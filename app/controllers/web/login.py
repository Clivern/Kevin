"""
Login Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

class Login(View):

    template_name = 'templates/login.html'

    def get(self, request):
        return render(request, self.template_name, {'page_title': 'Login'})