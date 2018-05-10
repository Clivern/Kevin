"""
Namespace Web Controller
"""

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


class Namespace(View):

    template_name = 'templates/namespace.html'


    def get(self, request, namespace):
        return render(request, self.template_name, {'page_title': _('Namespace')})