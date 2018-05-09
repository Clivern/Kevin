"""
Helpers Module
"""

import json
import logging
from django.utils import timezone
from datetime import timedelta
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

    def time_after(self, interval):
        datetime = timezone.now()
        for key, value in interval.items():
            if key == "microseconds":
                datetime += timedelta(microseconds=value)
            elif key == "milliseconds":
                datetime += timedelta(milliseconds=value)
            elif key == "seconds":
                datetime += timedelta(seconds=value)
            elif key == "minutes":
                datetime += timedelta(minutes=value)
            elif key == "hours":
                datetime += timedelta(hours=value)
            elif key == "days":
                datetime += timedelta(days=value)
            elif key == "weeks":
                datetime += timedelta(weeks=value)
            elif key == "months":
                datetime += timedelta(days=value * 30)
            elif key == "years":
                datetime += timedelta(days=value * 360)
        return datetime