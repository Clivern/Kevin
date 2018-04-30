"""
Login API Endpoint
"""

from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from app.modules.validation.form import Form
from app.modules.util.helpers import Helpers
from app.modules.core.login import Login as Login_Core
from app.modules.core.request import Request
from app.modules.core.response import Response
from django.utils.translation import gettext as _
from django.urls import reverse

#@method_decorator(csrf_exempt, name='dispatch')
class Login(View):

    _request = None
    _response = None
    _helpers = None
    _form = None
    _login = None
    _logger = None

    def __init__(self):
        self._helpers = Helpers()
        self._form = Form()
        self._login = Login_Core()
        self._request = Request()
        self._response = Response()
        self._logger = self._helpers.get_logger(__name__)

    def post(self, request):
        self._logger.debug(_("Request Method: POST"))
        self._logger.debug(_("Request URL: ") + reverse("app.api.private.v1.login.endpoint"))

        if self._login.is_authenticated(request):
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! User is already authenticated.")
            }]))

        self._request.set_request(request)

        request_data = self._request.get_request_data("post", {
            "username" : "",
            "password" : ""
        })

        self._form.add_inputs({
            'username': {
                'value': request_data["username"],
                'sanitize': {
                    'escape': {},
                    'strip': {}
                },
                'validate': {
                    'username_or_email': {
                        'error': _("Error! Username or password is invalid.")
                    }
                }
            },
            'password': {
                'value': request_data["password"],
                'validate': {
                    'password': {
                        'error': _("Error! Username or password is invalid.")
                    },
                    'length_between':{
                        'param': [7, 20],
                        'error': _("Error! Username or password is invalid.")
                    }
                }
            }
        })

        self._form.process()

        if not self._form.is_passed():
            return JsonResponse(self._response.send_private_failure(self._form.get_errors(with_type=True)))

        if self._login.authenticate(self._form.get_input_value("username"), self._form.get_input_value("password"), request):
            return JsonResponse(self._response.send_private_success([{
                "type": "success",
                "message": _("You logged in successfully.")
            }]))
        else:
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Username or password is invalid.")
            }]))