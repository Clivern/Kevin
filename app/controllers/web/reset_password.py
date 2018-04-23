"""
Reset Password Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

class Reset_Password(View):

    template_name = 'templates/reset_password.html'

    def get(self, request, token):
        return render(request, self.template_name, {'page_title': 'Reset Password'})