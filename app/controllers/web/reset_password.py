"""
Reset Password Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from app.modules.core.decorators import redirect_if_authenticated
from app.modules.core.reset_password import Reset_Password as Reset_Password_Module

class Reset_Password(View):

    template_name = 'templates/reset_password.html'
    _reset_password_core = None


    def __init__(self):
        self._reset_password_core = Reset_Password_Module()


    @redirect_if_authenticated
    def get(self, request, token):

        if not self._reset_password_core.check_token(token):
            messages.error(request, _("Reset token is expired or invalid, Please request another token!"))
            return redirect("app.web.forgot_password")

        return render(request, self.template_name, {'page_title': _('Reset Password'), 'reset_token': token})