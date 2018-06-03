"""
Endpoint Web Controller
"""

# standard library
import os

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _

# local Django
from app.modules.core.context import Context
from app.modules.core.statistics import NamespacesStatistics
from app.modules.core.statistics import EndpointsStatistics
from app.modules.core.endpoint import Endpoint as Endpoint_Module
from app.modules.core.namespace import Namespace as Namespace_Module


class Endpoint_View(View):

    template_name = 'templates/admin/namespaces/endpoints/view.html'
    __context = Context()
    __namespace_module = Namespace_Module()
    __namespaces_statistics = NamespacesStatistics()
    __endpoint_module = Endpoint_Module()
    __endpoints_statistics = EndpointsStatistics()


    def get(self, request, namespace_slug, endpoint_id):

        namespace = self.__namespace_module.get_one_by_slug(namespace_slug)

        if namespace == False or request.user.id != namespace.user.id:
            raise Http404("Namespace not found.")

        endpoint = self.__endpoint_module.get_one_by_id(endpoint_id)

        if endpoint == False or namespace.id != endpoint.namespace.id:
            raise Http404("Endpoint not found.")

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("%s Endpoint Activity · %s") % ("Item", self.__context.get("app_name", os.getenv("APP_NAME", "Kevin"))),
            "namespace": namespace,
            "endpoint": endpoint
        })

        return render(request, self.template_name, self.__context.get())



class Endpoint_Add(View):

    template_name = 'templates/admin/namespaces/endpoints/add.html'
    __context = Context()
    __context = Context()
    __namespace_module = Namespace_Module()
    __endpoint_module = Endpoint_Module()


    def get(self, request, namespace_slug):

        namespace = self.__namespace_module.get_one_by_slug(namespace_slug)

        if namespace == False or request.user.id != namespace.user.id:
            raise Http404("Namespace not found.")

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("Create Endpoint · %s") % (self.__context.get("app_name", os.getenv("APP_NAME", "Kevin"))),
            "namespace": namespace
        })

        return render(request, self.template_name, self.__context.get())



class Endpoint_Edit(View):

    template_name = 'templates/admin/namespaces/endpoints/edit.html'
    __context = Context()
    __context = Context()
    __namespace_module = Namespace_Module()
    __endpoint_module = Endpoint_Module()


    def get(self, request, namespace_slug, endpoint_id):

        namespace = self.__namespace_module.get_one_by_slug(namespace_slug)

        if namespace == False or request.user.id != namespace.user.id:
            raise Http404("Namespace not found.")

        endpoint = self.__endpoint_module.get_one_by_id(endpoint_id)

        if endpoint == False or namespace.id != endpoint.namespace.id:
            raise Http404("Endpoint not found.")

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("Edit Endpoint · %s") % (self.__context.get("app_name", os.getenv("APP_NAME", "Kevin"))),
            "namespace": namespace,
            "endpoint": endpoint
        })

        return render(request, self.template_name, self.__context.get())