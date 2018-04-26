"""
Locale Module
"""

from django.utils.translation import activate

class Locale():

    def switch_language(language):
        """Switch to another language"""
        activate(language)