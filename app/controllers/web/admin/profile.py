"""
Profile Web Controller
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
from app.modules.core.profile import Profile


class Profile(View):

    template_name = 'templates/admin/profile.html'
    _context = Context()
    _profile = Profile()
    _user = None


    def get(self, request):

        self._user_id = request.user.id

        self._context.autoload_options()
        self._context.push({
            "page_title": _("Profile | %s") % self._context.get("app_name", os.getenv("APP_NAME", "Kevin"))
        })

        self._context.push(self._profile.get_profile(self._user_id))

        return render(request, self.template_name, self._context.get())