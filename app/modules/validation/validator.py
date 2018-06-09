"""
Validator Module
"""

# standard library
import re
import uuid
import json

# third-party
from jsonschema import Draft3Validator
from jsonschema import Draft4Validator

# Django
from django.core.signing import Signer
from django.core.validators import validate_email
from django.core.validators import URLValidator

# Local Django
from app.modules.entity.namespace_entity import Namespace_Entity
from app.modules.entity.endpoint_entity import Endpoint_Entity


class Validator():

    __input = None


    def set_input(self, input_value):
        self.__input = input_value


    def empty(self):
        return self.__input == ''


    def not_empty(self):
        return not self.__input == ''


    def length_between(self, from_length, to_length):
        if to_length > len(self.__input) > from_length:
            return True
        else:
            return False


    def min_length(self, min_length):
        if len(self.__input) >= min_length:
            return True
        else:
            return False


    def max_length(self, max_length):
        if len(self.__input) <= max_length:
            return True
        else:
            return False


    def exact_length(self, exact_length):
        if len(self.__input) == exact_length:
            return True
        else:
            return False


    def greater_than(self, number):
        if int(self.__input) > number:
            return True
        else:
            return False


    def greater_than_equal(self, number):
        if int(self.__input) >= number:
            return True
        else:
            return False


    def less_than(self, number):
        if int(self.__input) < number:
            return True
        else:
            return False


    def less_than_equal(self, number):
        if int(self.__input) <= number:
            return True
        else:
            return False


    def equal(self, number):
        if int(self.__input) == number:
            return True
        else:
            return False


    def same_as(self, text):
        if self.__input == text:
            return True
        else:
            return False


    def any_of(self, options):
        return self.__input in options


    def all_of(self, options):
        if not len(options) == len(self.__input):
            return False
        status = True
        for item in self.__input:
            status &= item in options
        return status


    def none_of(self, options):
        return self.__input not in options


    def alpha(self):
        if not isinstance(self.__input, (str)):
            return False
        return self.__input.isalpha()


    def alpha_numeric(self):
        if not isinstance(self.__input, (str)):
            return False
        return self.__input.isalnum()


    def password(self):
        if re.search("[a-z]", self.__input) is None:
            return False
        if re.search("[A-Z]", self.__input) is None:
            return False
        if re.search("[0-9]", self.__input) is None:
            return False
        if not re.search("^[a-zA-Z0-9]*$", self.__input) is None:
            return False
        return True


    def names(self):
        return (re.search('[^a-zA-Z\s\-\']', self.__input) == None)


    def username_or_email(self):
        return self.email() or self.alpha_numeric()


    def namespace_slug(self):
        regex = re.compile('^[a-z0-9-_]+$')
        return bool(regex.match(self.__input))


    def namespace_name(self):
        regex = re.compile('^[a-zA-Z0-9-_\s]+$')
        return bool(regex.match(self.__input))


    def digit(self):
        if not isinstance(self.__input, (str)):
            return False
        return self.__input.isdigit()


    def email(self):
        try:
            return True if validate_email(self.__input) == None else False
        except Exception as e:
            return False


    def emails(self, sep=','):
        status = True
        for email in self.__input.split(sep):
            try:
                status &= True if validate_email(self.__input) == None else False
            except Exception as e:
                status &= False
        return status


    def url(self, protocols=['http', 'https']):
        validate = URLValidator(protocols)
        try:
            return True if validate(self.__input) == None else False
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
            return True if validate_ipv4_address(self.__input) == None else False
        except Exception as e:
            return False


    def ipv6(self):
        try:
            return True if validate_ipv6_address(self.__input) == None else False
        except Exception as e:
            return False


    def ipv46(self):
        try:
            return True if validate_ipv46_address(self.__input) == None else False
        except Exception as e:
            return False


    def uuid(self):
        try:
            uuid.UUID(self.__input)
            return True
        except:
            return False


    def matches(self, regex, flags=0):
        if isinstance(regex, (str)):
            regex = re.compile(regex, flags)

        return bool(regex.match(self.__input))


    def token(self):
        signer = Signer()
        try:
            original = signer.unsign(self.__input)
        except Exception as e:
            return False

        return True if original != "" else False


    def optional(self):
        return self.__input == ""


    def numeric(self):
        regex = re.compile('^[0-9]+$')
        return bool(regex.match(self.__input))


    def namespace_pk(self):
        regex = re.compile('^[0-9]+$')
        if not bool(regex.match(self.__input)):
            return False

        namespace_entity = Namespace_Entity()
        return namespace_entity.get_one_by_id(self.__input) != False


    def entity_pk(self):
        regex = re.compile('^[0-9]+$')
        if not bool(regex.match(self.__input)):
            return False

        endpoint_entity = Endpoint_Entity()
        return endpoint_entity.get_one_by_id(self.__input) != False


    def custom_endpoint_route(self):
        if self.__input.strip() == "":
            return False
        return True


    def custom_endpoint_route_rules(self):

        if self.__input == "":
            return True

        try:
            data = json.loads(self.__input)
        except:
            return False

        return True


    def custom_endpoint_headers_rules(self):

        if self.__input == "":
            return True

        try:
            data = json.loads(self.__input)
        except:
            return False

        conditions = [
            "EQUALS",
            "NOT_EQUALS",
            "CONTAINS",
            "IS_EMPTY",
            "NOT_EMPTY",
            "GREATER_THAN",
            "LESS_THAN"
        ]
        int_regex = re.compile('^[\-0-9]+$')

        status = True
        for item in data:

            if not "key" in item or not "condition" in item or not "value" in item:
                status &= False
                return False

            if item["key"].strip() == "":
                status &= False
                return False

            if item["condition"] == "" or not item["condition"] in conditions:
                status &= False
                return False

            if item["condition"] == "GREATER_THAN" and not bool(int_regex.match(item["value"])):
                status &= False
                return False

            if item["condition"] == "LESS_THAN" and not bool(int_regex.match(item["value"])):
                status &= False
                return False

        return status


    def custom_endpoint_body_rules(self):

        if self.__input == "":
            return True

        try:
            data = json.loads(self.__input)
        except Exception as e:
            return False

        draft3 = True
        draft4 = True

        try:
            Draft3Validator.check_schema(data)
        except Exception as e:
            draft3 = False

        try:
            Draft4Validator.check_schema(data)
        except Exception as e:
            draft4 = False

        return draft3 or draft4