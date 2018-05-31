"""
Namespaces API Endpoint
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


class Namespaces_List(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None
    __namespace_module = Namespace_Module()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def get(self, request):

        self.__user_id = request.user.id



class Namespace_Create(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None
    __namespace_module = Namespace_Module()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def post(self, request):

        self.__user_id = request.user.id

        request_data = self.__request.get_request_data("post", {
            "name" : "",
            "slug" : "",
            "is_public": "on"
        })

        self.__form.add_inputs({
            'name': {
                'value': request_data["name"],
                'validate': {
                    'namespace_name': {
                        'error': _("Error! Namespace Name is invalid.")
                    },
                    'length_between':{
                        'param': [3, 41],
                        'error': _("Error! Namespace slug length must be from 4 to 40 characters.")
                    }
                }
            },
            'slug': {
                'value': request_data["slug"],
                'validate': {
                    'namespace_slug': {
                        'error': _('Error! Namespace slug is not valid.')
                    },
                    'length_between':{
                        'param': [3, 21],
                        'error': _('Error! Namespace slug length must be from 4 to 20 characters.')
                    }
                }
            },
            'is_public': {
                'value': request_data["is_public"],
                'validate': {
                    'any_of':{
                        'param': ["on", "off"],
                        'error': _('Error! Is public value is invalid.')
                    }
                }
            }
        })

        self.__form.process()

        if not self.__form.is_passed():
            return JsonResponse(self.__response.send_private_failure(self.__form.get_errors(with_type=True)))

        if self.__namespace_module.slug_used(self.__form.get_input_value("slug")):
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Namespace slug is already used.")
            }]))

        result = self.__namespace_module.insert_one({
            "name": self.__form.get_input_value("name"),
            "slug": self.__form.get_input_value("slug"),
            "is_public": (self.__form.get_input_value("is_public") == "on"),
            "user_id": self.__user_id
        })

        if result:
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Namespace created successfully.")
            }]))

        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while creating namespace.")
            }]))



class Namespace_Edit(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None
    __namespace_id = None
    __namespace_module = Namespace_Module()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def put(self, request, namespace_id):

        self.__user_id = request.user.id
        self.__namespace_id = namespace_id

        if not self.__namespace_module.user_owns(self.__namespace_id, self.__user_id):
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Invalid Request.")
            }]))

        request_data = self.__request.get_request_data("post", {
            "name" : "",
            "slug" : "",
            "is_public": "on"
        })

        self.__form.add_inputs({
            'name': {
                'value': request_data["name"],
                'validate': {
                    'namespace_name': {
                        'error': _("Error! Namespace Name is invalid.")
                    },
                    'length_between':{
                        'param': [3, 41],
                        'error': _("Error! Namespace slug length must be from 4 to 40 characters.")
                    }
                }
            },
            'slug': {
                'value': request_data["slug"],
                'validate': {
                    'namespace_slug': {
                        'error': _('Error! Namespace slug is not valid.')
                    },
                    'length_between':{
                        'param': [3, 21],
                        'error': _('Error! Namespace slug length must be from 4 to 20 characters.')
                    }
                }
            },
            'is_public': {
                'value': request_data["is_public"],
                'validate': {
                    'any_of':{
                        'param': ["on", "off"],
                        'error': _('Error! Is public value is invalid.')
                    }
                }
            }
        })

        self.__form.process()

        if not self.__form.is_passed():
            return JsonResponse(self.__response.send_private_failure(self.__form.get_errors(with_type=True)))

        if self.__namespace_module.slug_used_elsewhere(self.__namespace_id, self.__form.get_input_value("slug")):
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Namespace slug is already used.")
            }]))

        result = self.__namespace_module.update_one_by_id(self.__namespace_id, {
            "name": self.__form.get_input_value("name"),
            "slug": self.__form.get_input_value("slug"),
            "is_public": (self.__form.get_input_value("is_public") == "on"),
            "user_id": self.__user_id
        })

        if result:
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Namespace updated successfully.")
            }]))

        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while creating namespace.")
            }]))



class Namespace_Delete(View):

    __request = Request()
    __response = Response()
    __helpers = Helpers()
    __form = Form()
    __logger = None
    __user_id = None
    __namespace_id = None
    __namespace_module = Namespace_Module()


    def __init__(self):
        self.__logger = self.__helpers.get_logger(__name__)


    def delete(self, request, namespace_id):

        self.__user_id = request.user.id
        self.__namespace_id = namespace_id

        if not self.__namespace_module.user_owns(self.__namespace_id, self.__user_id):
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Invalid Request.")
            }]))

        if self.__namespace_module.delete_namespace(namespace_id):
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Namespace deleted successfully.")
            }]))

        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while deleting a namespace.")
            }]))