"""
Home Web Controller
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
from app.modules.util.helpers import Helpers
from app.modules.entity.option_entity import Option_Entity
from app.modules.core.decorators import redirect_if_not_installed


class Home(View):

    template_name = 'templates/home.html'
    _context = Context()
    _option_entity = Option_Entity()


    @redirect_if_not_installed
    def get(self, request):

        self._context.autoload_options()
        self._context.push({
            "page_title": _("Home | %s") % self._context.get("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        return render(request, self.template_name, self._context.get())