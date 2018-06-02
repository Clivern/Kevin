"""
Namespaces Web Controller
"""

# standard library
import os

# Django
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.http import Http404

# local Django
from app.modules.core.context import Context
from app.modules.core.statistics import NamespacesStatistics
from app.modules.core.namespace import Namespace as Namespace_Module


class Namespaces_List(View):

    template_name = 'templates/admin/namespaces/list.html'
    __context = Context()
    __namespace_module = Namespace_Module()
    __namespaces_statistics = NamespacesStatistics()


    def get(self, request):

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("Namespaces · %s") % self.__context.get("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        self.__context.push({
            "namespaces": self.__namespace_module.get_many_by_user(request.user.id),
            "donut": self.__namespaces_statistics.overall_count_chart(request.user.id),
            "line_chart": self.__namespaces_statistics.count_over_time_chart(20, request.user.id)
        })

        return render(request, self.template_name, self.__context.get())


class Namespace_Create(View):

    template_name = 'templates/admin/namespaces/create.html'
    __context = Context()
    __namespace_module = Namespace_Module()


    def get(self, request):

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("Create a Namespace · %s") % self.__context.get("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        return render(request, self.template_name, self.__context.get())


class Namespace_Edit(View):

    template_name = 'templates/admin/namespaces/edit.html'
    __context = Context()
    __namespace_module = Namespace_Module()


    def get(self, request, namespace_slug):

        namespace = self.__namespace_module.get_one_by_slug(namespace_slug)

        if namespace == False or request.user.id != namespace.user.id:
            raise Http404("Namespace not found.")

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("Edit %s Namespace · %s") % (namespace.name, self.__context.get("app_name", os.getenv("APP_NAME", "Kevin"))),
            "namespace": namespace
        })

        return render(request, self.template_name, self.__context.get())



class Namespace_View(View):

    template_name = 'templates/admin/namespaces/view.html'
    __context = Context()
    __namespace_module = Namespace_Module()
    __namespaces_statistics = NamespacesStatistics()


    def get(self, request, namespace_slug):

        namespace = self.__namespace_module.get_one_by_slug(namespace_slug)

        if namespace == False or request.user.id != namespace.user.id:
            raise Http404("Namespace not found.")

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("%s Namespace · %s") % (namespace.name, self.__context.get("app_name", os.getenv("APP_NAME", "Kevin"))),
            "namespace": namespace,
            "donut": self.__namespaces_statistics.count_endpoints_by_target(namespace.id),
            "line_chart": self.__namespaces_statistics.count_requests_over_time_chart(20, namespace.id)
        })

        return render(request, self.template_name, self.__context.get())