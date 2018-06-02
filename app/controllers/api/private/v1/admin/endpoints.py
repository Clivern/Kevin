"""
Endpoints API Endpoint
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
from app.modules.core.endpoint import Endpoint as Endpoint_Module


class Endpoints(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None
    __endpoint_module = Endpoint_Module()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def get(self, request):

        self.__user_id = request.user.id


    def post(self, request):

        self.__user_id = request.user.id

        self.__request.set_request(request)



class Endpoint(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None
    __endpoint_id = None
    __endpoint_module = Endpoint_Module()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def post(self, request, endpoint_id):

        self.__user_id = request.user.id
        self.__endpoint_id = endpoint_id

        if not self.__endpoint_module.user_owns(self.__endpoint_id, self.__user_id):
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Invalid Request.")
            }]))

        self.__request.set_request(request)



    def delete(self, request, endpoint_id):

        self.__user_id = request.user.id
        self.__endpoint_id = endpoint_id

        if not self.__endpoint_module.user_owns(self.__endpoint_id, self.__user_id):
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Invalid Request.")
            }]))

        if self.__endpoint_module.delete_endpoint(self.__endpoint_id):
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Endpoint deleted successfully.")
            }]))

        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while deleting endpoint.")
            }]))