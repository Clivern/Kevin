"""
Register API Endpoint
"""

from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from app.modules.validation.form import Form
from app.modules.util.helpers import Helpers
from app.modules.core.register import Register as Register_Core
from app.modules.core.request import Request
from app.modules.core.response import Response
from django.utils.translation import gettext as _
from django.urls import reverse
from app.modules.core.decorators import stop_request_if_authenticated

class Register(View):

    _request = None
    _response = None
    _helpers = None
    _form = None
    _register = None
    _logger = None

    def __init__(self):
        self._helpers = Helpers()
        self._form = Form()
        self._register = Register_Core()
        self._request = Request()
        self._response = Response()
        self._logger = self._helpers.get_logger(__name__)

    @stop_request_if_authenticated
    def post(self, request):
        self._logger.debug(_("Request Method: POST"))
        self._logger.debug(_("Request URL: ") + reverse("app.api.private.v1.register.endpoint"))

        self._request.set_request(request)

        request_data = self._request.get_request_data("post", {
            "first_name" : "",
            "last_name" : "",
            "username" : "",
            "email" : "",
            "password" : ""
        })

        self._form.add_inputs({
            'first_name': {
                'value': request_data["first_name"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {
                    'names': {
                        'error': _('Error! First name contains invalid characters.')
                    },
                    'length_between':{
                        'param': [0, 20],
                        'error': _('Error! First name must be 1 to 20 characters long.')
                    }
                }
            },
            'last_name': {
                'value': request_data["last_name"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {
                    'names': {
                        'error': _('Error! Last name contains invalid characters.')
                    },
                    'length_between':{
                        'param': [0, 20],
                        'error': _('Error! Last name must be 1 to 20 characters long.')
                    }
                }
            },
            'username': {
                'value': request_data["username"],
                'sanitize': {
                    'escape': {},
                    'strip': {}
                },
                'validate': {
                    'alpha_numeric': {
                        'error': _('Error! Username must be alpha numeric.')
                    },
                    'length_between':{
                        'param': [4, 10],
                        'error': _('Error! Username must be 5 to 10 characters long.')
                    }
                }
            },
            'email': {
                'value': request_data["email"],
                'sanitize': {
                    'escape': {},
                    'strip': {}
                },
                'validate': {
                    'email': {
                        'error': _('Error! Admin email is invalid.')
                    }
                }
            },
            'password': {
                'value': request_data["password"],
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

        if self._register.username_used(self._form.get_input_value("username")):
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Username is already used.")
            }]))

        if self._register.email_used(self._form.get_input_value("email")):
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Email is already used for other account.")
            }]))

        result = self._register.create_user({
            "username": self._form.get_input_value("username"),
            "email": self._form.get_input_value("email"),
            "first_name": self._form.get_input_value("first_name"),
            "last_name": self._form.get_input_value("last_name"),
            "password": self._form.get_input_value("password"),
        })

        if result:
            return JsonResponse(self._response.send_private_success([{
                "type": "success",
                "message": _("Account created successfully.")
            }]))
        else:
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while creating your account.")
            }]))