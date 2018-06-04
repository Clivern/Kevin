"""
Requests API Endpoint
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
from app.modules.core.requests import Request as Request_Module


class Requests(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None
    __request_module = Request_Module()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def get(self, request):
        pass


class Request(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None
    __request_id = None
    __request_module = Request_Module()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def delete(self, request, request_id):

        self.__user_id = request.user.id
        self.__request_id = request_id
