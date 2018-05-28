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
    _context = Context()


    def get(self, request, namespace):

        self._context.autoload_options()
        self._context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self._context.push({
            "page_title": _("%s Endpoints | %s") % ("Item", self._context.get("app_name", os.getenv("APP_NAME", "Kevin")))
        })

        return render(request, self.template_name, self._context.get())


class Endpoint_View(View):

    template_name = 'templates/admin/namespaces/endpoints/view.html'
    _context = Context()


    def get(self, request, namespace, endpoint):

        self._context.autoload_options()
        self._context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self._context.push({
            "page_title": _("%s Endpoint Activity | %s") % ("Item", self._context.get("app_name", os.getenv("APP_NAME", "Kevin"))),
            "endpoint": endpoint
        })

        return render(request, self.template_name, self._context.get())