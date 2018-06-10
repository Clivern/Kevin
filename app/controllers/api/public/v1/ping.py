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

    __user_id = None
    __namespace_id = None
    __endpoint_id = None
    __body = None
    __headers = None
    __method = None
    __uri = None


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    @method_decorator(csrf_exempt)
    def dispatch(self, request, namespace_slug, endpoint_path):

        self.__headers = self.__get_headers(request)
        self.__method = request.method

        #curl -X GET -H "" -d '' "http://127.0.0.1:8000/mongo/33"
        #curl -X POST -H "" -d '' "http://127.0.0.1:8000/mongo/33"
        #curl -X HEAD -H "" -d '' "http://127.0.0.1:8000/mongo/33"
        #curl -X PUT -H "" -d '' "http://127.0.0.1:8000/mongo/33"
        #curl -X DELETE -H "" -d '' "http://127.0.0.1:8000/mongo/33"
        #curl -X PATCH -H "" -d '' "http://127.0.0.1:8000/mongo/33"
        #curl -X TRACE -H "" -d '' "http://127.0.0.1:8000/mongo/33"
        #curl -X OPTIONS -H "" -d '' "http://127.0.0.1:8000/mongo/33"
        #curl -X CONNECT -H "" -d '' "http://127.0.0.1:8000/mongo/33"

        namespace = self.__namespace_module.get_one_by_slug(namespace_slug)

        if namespace == False:
            return JsonResponse(self.__response.send_public_failure([{
                "error": "Error! Namespace not found."
            }]))

        if not namespace.is_public:
            if not "X-Auth-Token" in self.__headers:
                return JsonResponse(self.__response.send_public_failure([{
                    "error": "Error! Access Denied."
                }]))

            profile = self.__profile_module.get_profile_by_access_token(self.__headers["X-Auth-Token"])

            if profile == False:
                return JsonResponse(self.__response.send_public_failure([{
                    "error": "Error! Access Token Expired or Invalid."
                }]))

            if profile.user.id != namespace.user.id:
                return JsonResponse(self.__response.send_public_failure([{
                    "error": "Error! Access Denied."
                }]))

            self.__context.load_options({"reset_tokens_expire_after": 24})
            expire_after = int(self.__context.get("reset_tokens_expire_after", 24))

            if profile.access_token_updated_at < self.__helpers.time_after({"hours": -1}):
                return JsonResponse(self.__response.send_public_failure([{
                    "error": "Error! Access Token Expired."
                }]))

        print(self.__headers)
        print(namespace_slug)
        print("/%s" % endpoint_path)
        print(request.body)

        return JsonResponse(self.__response.send_public_success([{
            "status": "ok"
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