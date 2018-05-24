"""
Install API Endpoint
"""

# Django
from django.views import View
from django.urls import reverse
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# local Django
from app.modules.validation.form import Form
from app.modules.util.helpers import Helpers
from app.modules.core.request import Request
from app.modules.core.response import Response


class Profile(View):

    _request = Request()
    _response = Response()
    _helpers = Helpers()
    _form = Form()
    _settings = None
    _logger = None


    def __init__(self):
        self._logger = self._helpers.get_logger(__name__)


    def post(self, request):

        self._request.set_request(request)
        request_data = self._request.get_request_data("post", {
            "action" : ""
        })

        self._form.add_inputs({
            'action': {
                'value': request_data["action"],
                'validate': {
                    'any_of':{
                        'param': [["_update_profile", "_update_password", "_update_access_token", "_update_refresh_token"]],
                        'error': _("Error! Invalid Request.")
                    }
                }
            }
        })

        self._form.process()

        if not self._form.is_passed():
            return JsonResponse(self._response.send_private_failure(self._form.get_errors(with_type=True)))

        if self._form.get_input_value("action") == "_update_profile":
            return self._update_profile(request)
        elif self._form.get_input_value("action") == "_update_password":
            return self._update_password(request)
        elif self._form.get_input_value("action") == "_update_access_token":
            return self._update_access_token(request)
        elif self._form.get_input_value("action") == "_update_refresh_token":
            return self._update_refresh_token(request)


    def _update_profile(self, request):
        pass


    def _update_password(self, request):
        pass


    def _update_access_token(self, request):
        pass


    def _update_refresh_token(self, request):
        pass
