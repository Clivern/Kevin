"""
Locale Module
"""

from django.utils.translation import activate

class Locale():

    def switch_language(language):
        activate(language)