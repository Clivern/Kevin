"""
Install Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.utils.translation import activate

class Install(View):

    template_name = 'templates/install.html'

    def get(self, request):
        activate('fr')
        return render(request, self.template_name, {'page_title': _('Installation')})