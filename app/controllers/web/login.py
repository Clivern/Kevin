"""
Login Web Controller
"""

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

# local Django
from app.modules.core.decorators import redirect_if_authenticated


class Login(View):

    template_name = 'templates/login.html'


    @redirect_if_authenticated
    def get(self, request):
        return render(request, self.template_name, {'page_title': _('Login')})