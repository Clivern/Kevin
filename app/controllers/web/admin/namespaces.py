"""
Namespaces Web Controller
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


    def get(self, request, namespace):

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("Edit %s Namespace | %s") % ("Item", self.__context.get("app_name", os.getenv("APP_NAME", "Kevin")))
        })

        return render(request, self.template_name, self.__context.get())