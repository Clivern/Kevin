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
    _context = Context()


    def get(self, request):

        self._context.autoload_options()
        self._context.push({
            "page_title": _("Namespaces | %s") % self._context.get("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        return render(request, self.template_name, self._context.get())


class Namespace_Create(View):

    template_name = 'templates/admin/namespaces/create.html'
    _context = Context()


    def get(self, request):

        self._context.autoload_options()
        self._context.push({
            "page_title": _("Create a Namespace | %s") % self._context.get("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        return render(request, self.template_name, self._context.get())


class Namespace_Edit(View):

    template_name = 'templates/admin/namespaces/edit.html'
    _context = Context()


    def get(self, request, namespace):

        self._context.autoload_options()
        self._context.push({
            "page_title": _("Edit %s Namespace | %s") % ("Item", self._context.get("app_name", os.getenv("APP_NAME", "Kevin")))
        })

        return render(request, self.template_name, self._context.get())