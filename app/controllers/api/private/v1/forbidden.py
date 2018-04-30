"""
Forbidden Access Views
"""

from django.http import JsonResponse
from app.modules.core.response import Response
from django.utils.translation import gettext as _

def csrf_failure(request, reason=""):
    response = Response()

    return JsonResponse(response.send_private_failure([{
        "type": "error",
        "message": _("Error! Something goes wrong during installing.")
    }]), status=403)