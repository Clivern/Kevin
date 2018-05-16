"""
Install API Endpoint
"""

# Django
from django.views import View
from django.urls import reverse
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# local Django
from app.modules.validation.form import Form
from app.modules.util.helpers import Helpers
from app.modules.core.request import Request
from app.modules.core.response import Response


class Settings(View):

    _request = Request()
    _response = Response()
    _helpers = Helpers()
    _form = Form()
    _settings = None
    _logger = None


    def __init__(self):
        self._logger = self._helpers.get_logger(__name__)


    def post(self, request):
        self._logger.debug(_("Request Method: POST"))
        self._logger.debug(_("Request URL: ") + reverse("app.api.private.v1.admin.settings.endpoint"))