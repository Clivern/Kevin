"""
Settings Web Controller
"""

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _

# local Django
from app.modules.core.context import Context


class Settings(View):

    template_name = 'templates/admin/settings.html'
    _context = Context()


    def get(self, request):

        self._context.push({'page_title': _('Settings')})

        return render(request, self.template_name, self._context.get())