"""
Register Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from app.modules.core.decorators import redirect_if_authenticated

class Register(View):

    template_name = 'templates/register.html'


    @redirect_if_authenticated
    def get(self, request):
        return render(request, self.template_name, {'page_title': _('Register')})