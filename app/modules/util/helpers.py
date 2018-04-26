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

    def switch_language(language):
        """Switch to another language"""
        activate(language)