"""
Errors Middleware
"""

# Django
from django.utils.translation import gettext as _

# local Django
from app.modules.util.helpers import Helpers


class Errors():

    _helpers = Helpers()
    _logger = None


    def __init__(self, get_response):
        self.get_response = get_response
        self._logger = self._helpers.get_logger(__name__)


    def __call__(self, request):

        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):
        self._logger.error(_("The server encountered something unexpected! %s %s  - %s - %s") % (request.method, request.path, exception.__class__.__name__, exception))
        return None