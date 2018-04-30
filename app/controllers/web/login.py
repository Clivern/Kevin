"""
Login Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from app.modules.core.login import Login as Login_Core

class Login(View):

    template_name = 'templates/login.html'
    _login = None

    def __init__(self):
        self._login = Login_Core()

    def get(self, request):
        if self._login.is_authenticated(request):
            return redirect("app.web.admin.dashboard")

        return render(request, self.template_name, {'page_title': _('Login')})