"""
Forgot Password API Endpoint
"""

from django.views import View
from django.http import JsonResponse
from app.modules.validation.form import Form
from app.modules.util.helpers import Helpers
from app.modules.core.forgot_password import Forgot_Password as Forgot_Password_Module
from app.modules.core.request import Request
from app.modules.core.response import Response
from django.utils.translation import gettext as _
from django.urls import reverse
from app.modules.core.decorators import stop_request_if_authenticated

class Forgot_Password(View):

    _request = None
    _response = None
    _helpers = None
    _form = None
    _logger = None
    _forgot_password = None

    def __init__(self):
        self._helpers = Helpers()
        self._form = Form()
        self._request = Request()
        self._response = Response()
        self._logger = self._helpers.get_logger(__name__)
        self._forgot_password = Forgot_Password_Module()

    @stop_request_if_authenticated
    def post(self, request):
        self._logger.debug(_("Request Method: POST"))
        self._logger.debug(_("Request URL: ") + reverse("app.api.private.v1.forgot_password.endpoint"))