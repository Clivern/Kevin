"""
Helpers Module
"""

from django.utils.text import slugify
from django.utils.translation import activate
import logging

class Helpers():

    def slugify(self, text, allow_unicode=False):
        """Create a slug"""
        return slugify(text, allow_unicode=allow_unicode)

    def get_logger(self, name = __name__):
        """Get Logger"""
        return logging.getLogger(name)

    def switch_language(self, language):
        """Switch to another language"""
        activate(language)

    def get_request_data(self, data_bag, predicted):
        request_data = {}

        for key, default in predicted.items():
            request_data[key] = data_bag[key] if key in data_bag else default

        return request_data