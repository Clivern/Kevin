"""
Custom Decorators
"""

from django.shortcuts import redirect
from django.http import JsonResponse
from app.modules.core.response import Response
from django.utils.translation import gettext as _

def redirect_if_authenticated(function):
    def wrap(controller, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return redirect("app.web.admin.dashboard")
        return function(controller, request, *args, **kwargs)
    return wrap

def stop_request_if_authenticated(function):
    def wrap(controller, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            response = Response()
            return JsonResponse(response.send_private_failure([{
                "type": "error",
                "message": _("Error! Access forbidden for authenticated users.")
            }]))
        return function(controller, request, *args, **kwargs)
    return wrap