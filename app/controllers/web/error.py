"""
Error Web Controller
"""

# standard library
import os

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _

# local Django
from app.modules.core.context import Context


def handler500(request, exception=None, template_name='templates/500.html'):

    template_name = 'templates/500.html'

    _context = Context()

    _context.autoload_options()
    _context.push({
        "page_title": _("500 | %s") % _context.get("app_name", os.getenv("APP_NAME", "Kevin"))
    })

    return render(request, template_name, _context.get(), status=500)