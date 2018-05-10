"""
Register Web Controller
"""

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

# local Django
from app.modules.core.context import Context
from app.modules.core.decorators import redirect_if_authenticated


class Register(View):

    template_name = 'templates/register.html'
    _context = Context()


    @redirect_if_authenticated
    def get(self, request):

        self._context.push({'page_title': _('Register')})

        return render(request, self.template_name, self._context.get())