"""
Context Module
"""

# local Django
from app.settings.info import *
from app.modules.entity.option_entity import Option_Entity


class Context():

    _data = {}
    _option_entity = Option_Entity()


    def __init__(self):
        self._data["AUTHOR"] = AUTHOR
        self._data["COPYRIGHT"] = COPYRIGHT
        self._data["LICENSE"] = LICENSE
        self._data["VERSION"] = VERSION
        self._data["MAINTAINER"] = MAINTAINER
        self._data["EMAIL"] = EMAIL
        self._data["STATUS"] = STATUS
        self._data["REPO_URL"] = REPO_URL
        self._data["AUTHOR_URL"] = AUTHOR_URL
        self._data["RELEASES"] = RELEASES
        self._data["SUPPORT_URL"] = SUPPORT_URL


    def push(self, new_data):
        self._data.update(new_data)


    def load_options(self, options):
        options_to_load = {}
        for key in options.keys():
            options_to_load[key] = options[key]
            if not key in self._data.keys():
                self._data[key] = options[key]

        if len(options_to_load.keys()) > 0:
            new_options = self._option_entity.get_many_by_keys(options_to_load.keys())
            for option in new_options:
                self._data[option.key] = option.value


    def autoload_options(self):
        options = self._option_entity.get_many_by_autoload(True)
        for option in options:
            self._data[option.key] = option.value


    def get(self, key = None, default = None):
        if key != None:
            return self._data[key] if key in self._data else default
        return self._data