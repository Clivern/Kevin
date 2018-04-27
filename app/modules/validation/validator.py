"""
Validator Module
"""

from __future__ import unicode_literals

import re
import uuid
import warnings


class Validator():
    """Validate Inputs Module"""

    # Input Value
    _input = None

    def set_input(self, input_value):
        """Set Input Value"""
        self._input = input_value

    def empty(self):
        """Validate if input has empty value"""
        return self._input == ''

    def not_empty(self):
        """Validate if input has no empty value"""
        return not self._input == ''

    def length_between(self, from_length, to_length):
        """Validate if input length is between provided length limits"""
        if to_length > len(self._input) > from_length:
            return True
        else:
            return False

    def min_length(self, min_length):
        """Validate if input length is greater that provided length"""
        if len(self._input) >= min_length:
            return True
        else:
            return False

    def max_length(self, max_length):
        """Validate if input length is less that provided length"""
        if len(self._input) <= max_length:
            return True
        else:
            return False

    def exact_length(self, exact_length):
        """Validate if input length is equal to provided one"""
        if len(self._input) == exact_length:
            return True
        else:
            return False

    def greater_than(self, number):
        """Validate if input is greater than provided one"""
        if self._input > number:
            return True
        else:
            return False

    def greater_than_equal(self, number):
        """Validate if input is greater than or equal provided one"""
        if self._input >= number:
            return True
        else:
            return False

    def less_than(self, number):
        """Validate if input is less than provided one"""
        if self._input < number:
            return True
        else:
            return False

    def less_than_equal(self, number):
        """Validate if input is less than or equal provided one"""
        if self._input <= number:
            return True
        else:
            return False

    def equal(self, number):
        """Validate if input is equal to provided one"""
        if self._input == number:
            return True
        else:
            return False

    def same_as(self, text):
        """Validate if input is the same as provided one"""
        if self._input == text:
            return True
        else:
            return False

    def any_of(self, options):
        """Validate if input in a list"""
        return self._input in options

    def all_of(self, options):
        """Validate if input is all of a list"""
        if not len(options) == len(self._input):
            return False
        status = True
        for item in self._input:
            status &= item in options
        return status

    def none_of(self, options):
        """Validate if input not in a list"""
        return self._input not in options

    def alpha(self):
        """Validate if input is alpha"""
        if not isinstance(self._input, (str)):
            return False
        return self._input.isalpha()

    def alpha_numeric(self):
        """Validate if input is alpha numeric"""
        if not isinstance(self._input, (str)):
            return False
        return self._input.isalnum()

    def digit(self):
        """Validate if input is digits"""
        if not isinstance(self._input, (str)):
            return False
        return self._input.isdigit()

    def email(self):
        """Validate if input is a valid email address"""
        return bool(re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,5})$', self._input, re.IGNORECASE))

    def emails(self, sep=','):
        """Validate if input is a valid list of email addresses"""
        status = True
        for email in self._input.split(sep):
            status &= bool(re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,5})$', email, re.IGNORECASE))
        return status

    def url(self, protocols=['http', 'https']):
        """Validate if input is a valid URL"""
        regex = re.compile(
            r'^(?:' + '|'.join(protocols) + ')://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return bool(regex.match(self._input))

    def ip(self, formats=['ipv4']):
        """Validates an IP address."""
        if 'ipv4' in formats:
            return self.ipv4()
        else:
            return False

    def ipv4(self):
        """Validates an IPv4 address."""
        parts = self._input.split('.')
        if len(parts) == 4 and all(x.isdigit() for x in parts):
            numbers = list(int(x) for x in parts)
            return all(num >= 0 and num < 256 for num in numbers)
        return False

    def uuid(self):
        """Validates if input is a UUID"""
        try:
            uuid.UUID(self._input)
            return True
        except:
            return False

    def matches(self, regex, flags=0):
        """Validate if input match the provided regexp"""
        if isinstance(regex, (str)):
            regex = re.compile(regex, flags)

        return bool(regex.match(self._input))