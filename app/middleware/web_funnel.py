"""
Logging Middleware
"""

# Django
from django.shortcuts import redirect
from django.http import JsonResponse
from django.utils.translation import gettext as _

# local Django
from app.modules.util.helpers import Helpers
from app.modules.core.funnel import Funnel
from app.modules.core.response import Response
from app.modules.entity.option_entity import Option_Entity


class Web_Funnel():

    _helpers = Helpers()
    _logger = None
    _funnel = Funnel()
    _roles = {

    }


    def __init__(self, get_response):
        self.get_response = get_response
        self._logger = self._helpers.get_logger(__name__)


    def __call__(self, request):

        self._funnel.set_rules(self._roles)
        self._funnel.set_request(request)

        if self._funnel.action_needed():
            return self._funnel.fire()

        response = self.get_response(request)

        return response