"""
Install Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from app.modules.core.install import Install as Install_Core

class Install(View):

    template_name = 'templates/install.html'
    _install = None


    def __init__(self):
        self._install = Install_Core()


    def get(self, request):
        if self._install.is_installed():
            return redirect("app.web.login")

        return render(request, self.template_name, {'page_title': _('Installation')})