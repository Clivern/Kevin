"""
Login Web Controller
"""

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

# local Django
from app.modules.core.context import Context
from app.modules.core.decorators import redirect_if_authenticated
from app.modules.core.decorators import redirect_if_not_installed


class Login(View):

    template_name = 'templates/login.html'
    _context = Context()

    @redirect_if_not_installed
    @redirect_if_authenticated
    def get(self, request):

        self._context.push({'page_title': _('Login')})

        return render(request, self.template_name, self._context.get())