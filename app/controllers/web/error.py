"""
Error Web Controller
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
from app.modules.entity.option_entity import Option_Entity


class Error(View):

    template_name = 'templates/500.html'
    _context = Context()
    _option_entity = Option_Entity()


    def get(self, request):

        self._context.push({
            "page_title": _("500 | %s") % self._option_entity.get_value_by_key("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        return render(request, self.template_name, self._context.get(), status=500)