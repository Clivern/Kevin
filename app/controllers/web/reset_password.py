"""
Reset Password Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from app.modules.core.decorators import redirect_if_authenticated

class Reset_Password(View):

    template_name = 'templates/reset_password.html'

    def __init__(self):
        pass

    @redirect_if_authenticated
    def get(self, request, token):
        return render(request, self.template_name, {'page_title': _('Reset Password'), 'reset_token': token})