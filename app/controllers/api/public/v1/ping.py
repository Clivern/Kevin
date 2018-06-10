"""
Ping API Endpoint
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
from app.modules.core.namespace import Namespace as Namespace_Module
from app.modules.core.endpoint import Endpoint as Endpoint_Module
from app.modules.core.requests import Request as Request_Module
from app.modules.core.profile import Profile as Profile_Module
from app.modules.core.context import Context


class Ping(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None

    __namespace_module = Namespace_Module()
    __endpoint_module = Endpoint_Module()
    __request_module = Request_Module()
    __profile_module = Profile_Module()
    __context = Context()

    __headers = None


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    @method_decorator(csrf_exempt)
    def dispatch(self, request, endpoint_path):
        path_items = endpoint_path.split("/")
        namespace_slug = path_items[0]
        endpoint_path = endpoint_path.replace(namespace_slug, "").lstrip("/")

        self.__headers = self.__get_headers(request)

        namespace = self.__namespace_module.get_one_by_slug(namespace_slug)

        if namespace == False:
            return JsonResponse(self.__response.send_public_failure([{
                "error": "Error! Namespace not found."
            }]))

        if not namespace.is_public:
            if not "KVN-Auth-Token" in self.__headers:
                return JsonResponse(self.__response.send_public_failure([{
                    "error": "Error! Access Denied."
                }]))

            profile = self.__profile_module.get_profile_by_access_token(self.__headers["KVN-Auth-Token"])

            if profile == False:
                return JsonResponse(self.__response.send_public_failure([{
                    "error": "Error! Access Token Expired or Invalid."
                }]))

            if profile.user.id != namespace.user.id:
                return JsonResponse(self.__response.send_public_failure([{
                    "error": "Error! Access Denied."
                }]))

            self.__context.load_options({"access_tokens_expire_after": 24})
            expire_after = int(self.__context.get("access_tokens_expire_after", 24))

            if profile.access_token_updated_at < self.__helpers.time_after({"hours": -24}):
                return JsonResponse(self.__response.send_public_failure([{
                    "error": "Error! Access Token Expired."
                }]))


        result = self.__request_module.store_request({
            "method": request.method,
            "uri": endpoint_path,
            "headers": self.__headers,
            "body": request.body.decode('utf-8'),
            "namespace": namespace
        })

        if result:
            return JsonResponse(self.__response.send_public_success([]))
        else:
            return JsonResponse(self.__response.send_public_failure([{
                "error": "Error! Endpoint not found."
            }]))


    def __get_headers(self, request):
        headers = {
            "Content-Length": request.META['CONTENT_LENGTH'],
            "Content-Type": request.META['CONTENT_TYPE']
        }
        for header, value in request.META.items():
            if not header.startswith('HTTP'):
                continue
            header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
            headers[header] = value

        return headers