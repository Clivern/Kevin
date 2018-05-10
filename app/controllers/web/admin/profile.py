"""
Profile Web Controller
"""

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


class Profile(View):

    template_name = 'templates/profile.html'


    def get(self, request):
        return render(request, self.template_name, {'page_title': _('Profile')})