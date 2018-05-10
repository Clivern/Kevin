"""
Not Found Web Controller
"""

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _

# local Django
from app.modules.core.context import Context


class Not_Found(View):

    template_name = 'templates/404.html'
    _context = Context()


    def get(self, request):

        self._context.push({'page_title': _('404')})

        return render(request, self.template_name, self._context.get(), status=404)