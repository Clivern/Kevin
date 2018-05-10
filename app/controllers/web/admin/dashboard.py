"""
Dashboard Web Controller
"""

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


class Dashboard(View):

    template_name = 'templates/admin/dashboard.html'


    def get(self, request):
        return render(request, self.template_name, {'page_title': _('Dashboard')})