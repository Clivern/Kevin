"""
Logging Middleware
"""

# Django
from django.utils.translation import gettext as _

# local Django
from app.modules.util.helpers import Helpers


class Logging:

    _helpers = Helpers()
    _logger = None


    def __init__(self, get_response):
        self.get_response = get_response
        self._logger = self._helpers.get_logger(__name__)


    def __call__(self, request):
        self._logger.debug(_("Request Method: %s") % request.method)
        self._logger.debug(_("Request URL: %s") % request.path)
        self._logger.debug(_("Request Body: %s") % request.body)

        response = self.get_response(request)

        return response