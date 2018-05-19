"""
Not Found Web Controller
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
from app.modules.entity.option_entity import Option_Entity


def handler404(request, exception=None, template_name='templates/404.html'):

    template_name = 'templates/404.html'

    _context = Context()

    _context.autoload_options()
    _context.push({
        "page_title": _("404 | %s") % _context.get("app_name", os.getenv("APP_NAME", "Kevin"))
    })

    return render(request, template_name, _context.get(), status=404)