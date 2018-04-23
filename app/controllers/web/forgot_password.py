"""
Forgot Password Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _

class Forgot_Password(View):

    template_name = 'templates/forgot_password.html'

    def get(self, request):
        return render(request, self.template_name, {'page_title': _('Forgot Password')})