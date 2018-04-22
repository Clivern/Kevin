"""
Install API Endpoint
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

class Install(View):

    def post(self, request):
        return render(request, self.template_name, {'page_title': 'Dashboard'})