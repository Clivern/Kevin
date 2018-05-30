"""
Funnel Module
"""

# Django
from django.utils.translation import gettext as _

# local Django
from app.modules.util.helpers import Helpers


class Funnel():

    _helpers = Helpers()
    _logger = None
    _rules = {}
    _request = {}


    def __init__(self):
        self._logger = self._helpers.get_logger(__name__)


    def set_rules(self, rules):
        self._rules = rules


    def set_request(self, request):
        self._request = request


    def action_needed(self):
        return False


    def fire(self):
        pass


    def _parse(self):
        #_route_name = request.resolver_match.url_name
        #if request.user and request.user.is_authenticated:
        #    self._is_auth = True
        #    self._user_id = request.user.id
        #    self._username = request.user
        pass