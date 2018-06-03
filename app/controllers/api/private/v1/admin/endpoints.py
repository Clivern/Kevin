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
from app.modules.core.namespace import Namespace as Namespace_Module


class Endpoints(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None
    __endpoint_module = Endpoint_Module()
    __namespace_module = Namespace_Module()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    #def get(self, request):
    #    pass


    def post(self, request):

        self.__user_id = request.user.id
        self.__request.set_request(request)

        request_data = self.__request.get_request_data("post", {
            "namespace_id" : "",
            "route" : "",
            "method" : "",
            "target": "",
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
        })

        self.__form.add_inputs({
            'namespace_id': {
                'value': request_data["namespace_id"],
                'validate': {}
            },
            'route': {
                'value': request_data["route"],
                'validate': {}
            },
            'method': {
                'value': request_data["method"],
                'validate': {}
            },
            'target': {
                'value': request_data["target"],
                'validate': {}
            },
            'route_rules': {
                'value': request_data["route_rules"],
                'validate': {}
            },
            'headers_rules': {
                'value': request_data["headers_rules"],
                'validate': {}
            },
            'body_rules': {
                'value': request_data["body_rules"],
                'validate': {}
            }
        })

        self.__form.process()

        if not self.__form.is_passed():
            return JsonResponse(self.__response.send_private_failure(self.__form.get_errors(with_type=True)))

        if not self.__namespace_module.user_owns(self.__form.get_input_value("namespace_id"), self.__user_id):
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Invalid Request.")
            }]))

        result = self.__endpoint_module.insert_one({
            "namespace_id": self.__form.get_input_value("namespace_id"),
            "route": self.__form.get_input_value("route"),
            "method": self.__form.get_input_value("method"),
            "target": self.__form.get_input_value("target"),
            "route_rules": self.__form.get_input_value("route_rules"),
            "headers_rules": self.__form.get_input_value("headers_rules"),
            "body_rules": self.__form.get_input_value("body_rules")
        })

        if result:
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Endpoint created successfully.")
            }]))

        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while creating endpoint.")
            }]))



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

        request_data = self.__request.get_request_data("post", {
            "route" : "",
            "method" : "",
            "target": "",
            "route_rules": "{}",
            "headers_rules": "{}",
            "body_rules": "{}",
        })

        self.__form.add_inputs({
            'route': {
                'value': request_data["route"],
                'validate': {}
            },
            'method': {
                'value': request_data["method"],
                'validate': {}
            },
            'target': {
                'value': request_data["target"],
                'validate': {}
            },
            'route_rules': {
                'value': request_data["route_rules"],
                'validate': {}
            },
            'headers_rules': {
                'value': request_data["headers_rules"],
                'validate': {}
            },
            'body_rules': {
                'value': request_data["body_rules"],
                'validate': {}
            }
        })

        self.__form.process()

        if not self.__form.is_passed():
            return JsonResponse(self.__response.send_private_failure(self.__form.get_errors(with_type=True)))

        result = self.__endpoint_module.update_one_by_id(self.__endpoint_id, {
            "route": self.__form.get_input_value("route"),
            "method": self.__form.get_input_value("method"),
            "target": self.__form.get_input_value("target"),
            "route_rules": self.__form.get_input_value("route_rules"),
            "headers_rules": self.__form.get_input_value("headers_rules"),
            "body_rules": self.__form.get_input_value("body_rules")
        })

        if result:
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Endpoint updated successfully.")
            }]))

        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while creating endpoint.")
            }]))



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