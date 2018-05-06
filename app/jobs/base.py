"""
Base Job
"""

from app.modules.util.helpers import Helpers
from app.modules.entity.option_entity import Option_Entity

class Base():

    _option_entity = None
    _helpers = None
    _logger = None
    _arguments = {
        "app_name": "",
        "app_email": "",
        "app_url": ""
    }

    def __init__(self, arguments):
        self._helpers = Helpers()
        self._logger = self._helpers.get_logger(__name__)
        self._arguments.update(arguments)
        self._option_entity = Option_Entity()
        self._load_options()

    def _load_options(self):
        options = self._option_entity.get_many_by_keys(["app_name", "app_email", "app_url"])
        for option in options:
            if option.key in self._arguments.keys():
                self._arguments[option.key] = option.value