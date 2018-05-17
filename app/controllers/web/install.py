"""
Install Web Controller
"""

# standard library
import os

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.translation import gettext as _

# local Django
from app.modules.core.context import Context
from app.modules.entity.option_entity import Option_Entity
from app.modules.core.install import Install as Install_Module


class Install(View):

    template_name = 'templates/install.html'
    _install = None
    _context = Context()
    _install = Install_Module()
    _option_entity = Option_Entity()


    def get(self, request):

        if self._install.is_installed():
            return redirect("app.web.login")

        self._context.push({
            "page_title": _("Installation | %s") % self._option_entity.get_value_by_key("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        return render(request, self.template_name, self._context.get())