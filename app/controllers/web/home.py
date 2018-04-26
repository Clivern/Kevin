"""
Home Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from app.modules.util.helpers import Helpers

class Home(View):

    template_name = 'templates/home.html'

    def get(self, request):
        return render(request, self.template_name, {'page_title': 'Home'})