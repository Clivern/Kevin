"""
Endpoint Web Controller
"""

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


class Endpoint(View):

    template_name = 'templates/endpoint.html'


    def get(self, request, namespace, endpoint):
        return render(request, self.template_name, {'page_title': _('Endpoint'), "endpoint": endpoint})