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


from app.modules.core.upgrade import Upgrade

class Home(View):

    template_name = 'templates/home.html'
    __context = Context()
    __option_entity = Option_Entity()


    @redirect_if_not_installed
    def get(self, request):

        self.__context.autoload_options()
        self.__context.push({
            "page_title": _("Home · %s") % self.__context.get("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        return render(request, self.template_name, self.__context.get())