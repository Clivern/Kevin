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


class Namespaces(View):

    template_name = 'templates/admin/namespaces/list.html'
    _context = Context()


    def get(self, request):

        self._context.autoload_options()
        self._context.push({
            "page_title": _("Namespaces | %s") % self._context.get("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        return render(request, self.template_name, self._context.get())