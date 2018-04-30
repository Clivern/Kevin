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

@method_decorator(csrf_exempt, name='dispatch')
class Install(View):

    _request = None
    _request_data = {}

    _helpers = None
    _form = None

    def __init__(self):
        self._helpers = Helpers()
        self._form = Form()

    def post(self, request):
        self._request = request
        self._request_data = self._helpers.get_request_data(self._request.POST, {
            "app_name" : "",
            "app_email" : "",
            "admin_username" : "",
            "admin_email" : "",
            "admin_password" : ""
        })

        print(self._request_data)

        return JsonResponse({"status":"d"})