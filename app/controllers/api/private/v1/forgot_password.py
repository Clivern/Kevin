"""
Forgot Password API Endpoint
"""

# Django
from django.views import View
from django.urls import reverse
from django.http import JsonResponse
from django.utils.translation import gettext as _

# local Django
from app.modules.util.helpers import Helpers
from app.modules.core.request import Request
from app.modules.validation.form import Form
from app.modules.core.response import Response
from app.modules.core.decorators import stop_request_if_authenticated
from app.modules.core.forgot_password import Forgot_Password as Forgot_Password_Module


class Forgot_Password(View):

    _request = None
    _response = None
    _helpers = None
    _form = None
    _logger = None
    _forgot_password = None


    def __init__(self):
        self._helpers = Helpers()
        self._form = Form()
        self._request = Request()
        self._response = Response()
        self._logger = self._helpers.get_logger(__name__)
        self._forgot_password = Forgot_Password_Module()


    @stop_request_if_authenticated
    def post(self, request):
        self._logger.debug(_("Request Method: POST"))
        self._logger.debug(_("Request URL: ") + reverse("app.api.private.v1.forgot_password.endpoint"))

        self._request.set_request(request)

        request_data = self._request.get_request_data("post", {
            "email" : ""
        })

        self._form.add_inputs({
            'email': {
                'value': request_data["email"],
                'sanitize': {
                    'escape': {},
                    'strip': {}
                },
                'validate': {
                    'email': {
                        'error': _('Error! Email is invalid.')
                    }
                }
            }
        })

        self._form.process()

        if not self._form.is_passed():
            return JsonResponse(self._response.send_private_failure(self._form.get_errors(with_type=True)))

        if not self._forgot_password.check_email(self._form.get_input_value("email")):
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Email is not exist.")
            }]))

        reset_request = self._forgot_password.reset_request_exists(self._form.get_input_value("email"))

        if reset_request != False:
            if self._forgot_password.is_spam(reset_request):
                return JsonResponse(self._response.send_private_failure([{
                    "type": "error",
                    "message": _("Sorry! You already exceeded the maximum number of reset requests!")
                }]))
            token = self._forgot_password.update_request(reset_request)
        else:
            token = self._forgot_password.create_request(self._form.get_input_value("email"))

        if token == False:
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while creating reset request.")
            }]))


        message = self._forgot_password.send_message(self._form.get_input_value("email"), token)

        if message == False:
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while sending reset instructions.")
            }]))
        else:
            return JsonResponse(self._response.send_private_success([{
                "type": "success",
                "message": _("Reset instructions sent successfully.")
            }]))