"""
Request Module
"""

from app.modules.util.helpers import Helpers

class Request():

    _request = None
    _helpers = None
    _logger = None

    def __init__(self, request = None):
        self._request = request
        self._helpers = Helpers()
        self._logger = self._helpers.get_logger(__name__)

    def set_request(self, request):
        self._request = request

    def get_request_data(self, method, predicted):
        request_data = {}
        data_bag = self._request.POST if method.lower() == "post" else self._request.GET

        for key, default in predicted.items():
            request_data[key] = data_bag[key] if key in data_bag else default

        self._logger.debug("App Incoming Request: " + self._helpers.json_dumps(request_data))
        return request_data