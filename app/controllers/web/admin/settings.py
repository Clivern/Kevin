"""
Settings Web Controller
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


class Settings(View):

    template_name = 'templates/admin/settings.html'
    _context = Context()


    def get(self, request):

        self._context.autoload_options()
        self._context.load_options({
            "app_name": "",
            "app_email": "",
            "app_url": "",
            "app_description": "",
            "google_analytics_account": "",
            "reset_mails_messages_count": "",
            "reset_mails_expire_after": ""
        })
        self._context.push({
            "page_title": _("Settings | %s") % self._context.get("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        return render(request, self.template_name, self._context.get())