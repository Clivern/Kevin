"""
Endpoint Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

class Endpoint(View):

    template_name = 'templates/endpoint.html'

    def get(self, request, endpoint):
        return render(request, self.template_name, {'page_title': 'Endpoint', "endpoint": endpoint})