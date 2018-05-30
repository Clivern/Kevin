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


class Endpoints_List(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def post(self, request):

        self.__user_id = request.user.id


class Endpoint_Create(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def post(self, request):

        self.__user_id = request.user.id


class Endpoint_Edit(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def post(self, request):

        self.__user_id = request.user.id


class Endpoint_Delete(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def post(self, request):

        self.__user_id = request.user.id