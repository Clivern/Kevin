"""
Validator Module
"""

import re
import uuid
from django.core.validators import validate_email
from django.core.validators import URLValidator

class Validator():

    _input = None

    def set_input(self, input_value):
        self._input = input_value

    def empty(self):
        return self._input == ''

    def not_empty(self):
        return not self._input == ''

    def length_between(self, from_length, to_length):
        if to_length > len(self._input) > from_length:
            return True
        else:
            return False

    def min_length(self, min_length):
        if len(self._input) >= min_length:
            return True
        else:
            return False

    def max_length(self, max_length):
        if len(self._input) <= max_length:
            return True
        else:
            return False

    def exact_length(self, exact_length):
        if len(self._input) == exact_length:
            return True
        else:
            return False

    def greater_than(self, number):
        if self._input > number:
            return True
        else:
            return False

    def greater_than_equal(self, number):
        if self._input >= number:
            return True
        else:
            return False

    def less_than(self, number):
        if self._input < number:
            return True
        else:
            return False

    def less_than_equal(self, number):
        if self._input <= number:
            return True
        else:
            return False

    def equal(self, number):
        if self._input == number:
            return True
        else:
            return False

    def same_as(self, text):
        if self._input == text:
            return True
        else:
            return False

    def any_of(self, options):
        return self._input in options

    def all_of(self, options):
        if not len(options) == len(self._input):
            return False
        status = True
        for item in self._input:
            status &= item in options
        return status

    def none_of(self, options):
        return self._input not in options

    def alpha(self):
        if not isinstance(self._input, (str)):
            return False
        return self._input.isalpha()

    def alpha_numeric(self):
        if not isinstance(self._input, (str)):
            return False
        return self._input.isalnum()

    def password(self):
        if re.search("[a-z]", self._input) is None:
            return False
        if re.search("[A-Z]", self._input) is None:
            return False
        if re.search("[0-9]", self._input) is None:
            return False
        if not re.search("^[a-zA-Z0-9]*$", self._input) is None:
            return False
        return True

    def names(self):
        return (re.search('[^a-zA-Z\s\-\']', self._input) == None)

    def username_or_email(self):
        return self.email() or self.alpha_numeric()

    def digit(self):
        if not isinstance(self._input, (str)):
            return False
        return self._input.isdigit()

    def email(self):
        try:
            return True if validate_email(self._input) == None else False
        except Exception as e:
            return False

    def emails(self, sep=','):
        status = True
        for email in self._input.split(sep):
            try:
                status &= True if validate_email(self._input) == None else False
            except Exception as e:
                status &= False
        return status

    def url(self, protocols=['http', 'https']):
        validate = URLValidator(protocols)
        try:
            return True if validate(self._input) == None else False
        except Exception as e:
            return False

    def ip(self, formats=['ipv4', 'ipv6']):
        if 'ipv4' in formats and 'ipv6' in formats:
            return self.ipv46()
        elif 'ipv6' in formats:
            return self.ipv6()
        elif 'ipv4' in formats:
            return self.ipv4()
        else:
            return False

    def ipv4(self):
        try:
            return True if validate_ipv4_address(self._input) == None else False
        except Exception as e:
            return False

    def ipv6(self):
        try:
            return True if validate_ipv6_address(self._input) == None else False
        except Exception as e:
            return False

    def ipv46(self):
        try:
            return True if validate_ipv46_address(self._input) == None else False
        except Exception as e:
            return False

    def uuid(self):
        try:
            uuid.UUID(self._input)
            return True
        except:
            return False

    def matches(self, regex, flags=0):
        if isinstance(regex, (str)):
            regex = re.compile(regex, flags)

        return bool(regex.match(self._input))