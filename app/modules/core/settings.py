"""
Settings Module
"""

# local Django
from app.modules.util.helpers import Helpers
from app.modules.entity.option_entity import Option_Entity


class Settings():

    _option_entity = Option_Entity()
    _helpers = Helpers()
    _logger = None


    def __init__(self):
        self._logger = self._helpers.get_logger(__name__)


    def update_options(self, options):
        status = True
        for key, value in options.items():
            status &= self._option_entity.update_value_by_key(key, value)
        return status