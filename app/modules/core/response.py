"""
Response Module
"""

# Django
from django.http import JsonResponse
from django.utils.translation import gettext as _

# local Django
from app.modules.util.helpers import Helpers


class Response():

    _private = {}
    _public = {}
    _helpers = None
    _logger = None


    def __init__(self):
        self._helpers = Helpers()
        self._logger = self._helpers.get_logger(__name__)


    def send_private_success(self, messages, payload={}):
        self._private["status"] = "success"
        self._private["messages"] = messages
        if len(payload) > 0:
            self._private["payload"] = payload

        self._logger.debug(_("App Response: ") + self._helpers.json_dumps(self._private) + "\n")
        return self._private


    def send_private_failure(self, messages, payload={}):
        self._private["status"] = "failure"
        self._private["messages"] = messages
        if len(payload) > 0:
            self._private["payload"] = payload

        self._logger.debug(_("App Response: ") + self._helpers.json_dumps(self._private) + "\n")
        return self._private