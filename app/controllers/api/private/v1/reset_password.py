"""
Forgot Password API Endpoint
"""

from django.views import View
from django.http import JsonResponse
from app.modules.validation.form import Form
from app.modules.util.helpers import Helpers
from app.modules.core.reset_password import Reset_Password as Reset_Password_Module
from app.modules.core.request import Request
from app.modules.core.response import Response
from django.utils.translation import gettext as _
from django.urls import reverse
from app.modules.core.decorators import stop_request_if_authenticated

class Reset_Password(View):

    _request = None
    _response = None
    _helpers = None
    _form = None
    _logger = None
    _reset_password = None


    def __init__(self):
        self._helpers = Helpers()
        self._form = Form()
        self._request = Request()
        self._response = Response()
        self._logger = self._helpers.get_logger(__name__)
        self._reset_password = Reset_Password_Module()


    @stop_request_if_authenticated
    def post(self, request):
        self._logger.debug(_("Request Method: POST"))
        self._logger.debug(_("Request URL: ") + reverse("app.api.private.v1.reset_password.endpoint"))

        self._request.set_request(request)

        request_data = self._request.get_request_data("post", {
            "reset_token" : "",
            "new_password" : ""
        })

        self._form.add_inputs({
            'reset_token': {
                'value': request_data["reset_token"],
                'sanitize': {
                    'escape': {},
                    'strip': {}
                },
                'validate': {}
            },
            'new_password': {
                'value': request_data["new_password"],
                'validate': {
                    'password': {
                        'error': _('Error! Password must contain at least uppercase letter, lowercase letter, numbers and special character.')
                    },
                    'length_between':{
                        'param': [7, 20],
                        'error': _('Error! Password length must be from 8 to 20 characters.')
                    }
                }
            }
        })

        self._form.process()

        if not self._form.is_passed():
            return JsonResponse(self._response.send_private_failure(self._form.get_errors(with_type=True)))

        if not self._reset_password.check_token(self._form.get_input_value("reset_token")):
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Reset token is expired or invalid.")
            }]))

        result = self._reset_password.reset_password(
            self._form.get_input_value("reset_token"),
            self._form.get_input_value("new_password")
        )

        result &= self._reset_password.delete_reset_request(self._form.get_input_value("reset_token"))

        if result == False:
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while resetting password.")
            }]))
        else:
            return JsonResponse(self._response.send_private_success([{
                "type": "success",
                "message": _("Password updated successfully.")
            }]))