"""
Base Job
"""

from app.modules.util.helpers import Helpers

class Base():

    _helpers = None
    _logger = None
    _arguments = {}

    def __init__(self, arguments):
        self._helpers = Helpers()
        self._logger = self._helpers.get_logger(__name__)
        self._arguments = arguments