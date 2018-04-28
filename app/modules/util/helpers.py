"""
Helpers Module
"""

import json
import logging
from django.utils.text import slugify
from django.utils.translation import activate

class Helpers():

    _loggers = {}

    def slugify(self, text, allow_unicode=False):
        return slugify(text, allow_unicode=allow_unicode)

    def get_logger(self, name = __name__):
        if name in self._loggers:
            return self._loggers[name]
        self._loggers[name] = logging.getLogger(name)
        return self._loggers[name]

    def switch_language(self, language):
        activate(language)

    def get_request_data(self, data_bag, predicted):
        request_data = {}

        for key, default in predicted.items():
            request_data[key] = data_bag[key] if key in data_bag else default

        return request_data

    def json_dumps(self, data):
        return json.dumps(data)