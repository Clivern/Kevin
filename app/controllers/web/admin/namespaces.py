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

# local Django
from app.modules.core.context import Context
from app.modules.core.namespace import Namespace as Namespace_Module


class Namespaces_List(View):

    template_name = 'templates/admin/namespaces/list.html'
    __context = Context()


    def get(self, request):

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("Namespaces | %s") % self.__context.get("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        return render(request, self.template_name, self.__context.get())


class Namespace_Create(View):

    template_name = 'templates/admin/namespaces/create.html'
    __context = Context()


    def get(self, request):

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("Create a Namespace | %s") % self.__context.get("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        return render(request, self.template_name, self.__context.get())


class Namespace_Edit(View):

    template_name = 'templates/admin/namespaces/edit.html'
    __context = Context()
    __namespace_module = Namespace_Module()


    def get(self, request, namespace_slug):

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("Edit %s Namespace | %s") % ("Item", self.__context.get("app_name", os.getenv("APP_NAME", "Kevin")))
        })

        namespace = self.__namespace_module.get_one_by_slug(namespace_slug)

        if namespace == False:
            return redirect("404")

        self.__context.push({
            "namespace_id": namespace.id,
            "namespace_slug": namespace.slug,
            "namespace_name": namespace.name,
            "namespace_is_public": namespace.is_public
        })

        return render(request, self.template_name, self.__context.get())