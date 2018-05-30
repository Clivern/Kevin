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


class Endpoints_List(View):

    template_name = 'templates/admin/namespaces/endpoints/list.html'
    __context = Context()


    def get(self, request, namespace):

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("%s Endpoints | %s") % ("Item", self.__context.get("app_name", os.getenv("APP_NAME", "Kevin")))
        })

        return render(request, self.template_name, self.__context.get())


class Endpoint_View(View):

    template_name = 'templates/admin/namespaces/endpoints/view.html'
    __context = Context()


    def get(self, request, namespace, endpoint):

        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.push({
            "page_title": _("%s Endpoint Activity | %s") % ("Item", self.__context.get("app_name", os.getenv("APP_NAME", "Kevin"))),
            "endpoint": endpoint
        })

        return render(request, self.template_name, self.__context.get())