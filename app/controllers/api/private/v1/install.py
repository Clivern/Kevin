"""
Install API Endpoint
"""

from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from pprint import pprint

from app.modules.validation.form import Form
from app.modules.util.helpers import Helpers
from app.modules.core.install import Install as Install_Core
from app.modules.core.request import Request
from app.modules.core.response import Response
from django.utils.translation import gettext as _
from django.urls import reverse

@method_decorator(csrf_exempt, name='dispatch')
class Install(View):

    _request = None
    _response = None
    _helpers = None
    _form = None
    _install = None
    _logger = None

    def __init__(self):
        self._helpers = Helpers()
        self._form = Form()
        self._install = Install_Core()
        self._request = Request()
        self._response = Response()
        self._logger = self._helpers.get_logger(__name__)

    def post(self, request):
        self._logger.debug("Request Method: POST")
        self._logger.debug("Request URL: " + reverse("app.api.private.v1.install.endpoint"))

        if self._install.is_installed():
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Application is already installed.")
            }]))

        self._request.set_request(request)

        request_data = self._request.get_request_data("post", {
            "app_name" : "",
            "app_email" : "",
            "app_url" : "",
            "admin_username" : "",
            "admin_email" : "",
            "admin_password" : ""
        })

        self._form.add_inputs({
            'app_name': {
                'value': request_data["app_name"],
                'sanitize': {
                    'escape': {}
                },
                'validate': {
                    'email': {
                        'error': 'Please provide a valid email.'
                    }
                }
            },
            'app_email': {
                'value': request_data["app_email"],
                'sanitize': {
                    'escape': {}
                },
                'validate': {
                    'email': {
                        'error': 'Please provide a valid email.'
                    }
                }
            },
            'app_url': {
                'value': request_data["app_url"],
                'sanitize': {
                    'escape': {}
                },
                'validate': {
                    'email': {
                        'error': 'Please provide a valid email.'
                    }
                }
            },
            'admin_username': {
                'value': request_data["admin_username"],
                'sanitize': {
                    'escape': {}
                },
                'validate': {
                    'email': {
                        'error': 'Please provide a valid email.'
                    }
                }
            },
            'admin_email': {
                'value': request_data["admin_email"],
                'sanitize': {
                    'escape': {}
                },
                'validate': {
                    'email': {
                        'error': 'Please provide a valid email.'
                    }
                }
            },
            'admin_password': {
                'value': request_data["admin_password"],
                'sanitize': {
                    'escape': {}
                },
                'validate': {
                    'email': {
                        'error': 'Please provide a valid email.'
                    }
                }
            }
        })

        self._form.process()

        if not self._form.is_passed():
            return JsonResponse(self._response.send_private_failure(self._form.get_errors(with_type=True)))

        self._install.set_app_data(
            self._form.get_input_value("app_name"),
            self._form.get_input_value("app_email"),
            self._form.get_input_value("app_url")
        )
        self._install.set_admin_data(
            self._form.get_input_value("admin_username"),
            self._form.get_input_value("admin_email"),
            self._form.get_input_value("admin_password")
        )

        if self._install.install():
            return JsonResponse(self._response.send_private_success([{
                "type": "success",
                "message": _("Application installed successfully.")
            }]))
        else:
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong during installing.")
            }]))