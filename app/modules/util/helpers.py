"""
Helpers Module
"""

from django.utils.text import slugify

class Helpers():

    def slugify(self, text, allow_unicode=False):
        return slugify(text, allow_unicode=allow_unicode)