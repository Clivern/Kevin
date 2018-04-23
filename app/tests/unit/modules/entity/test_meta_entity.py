"""
Meta Entity Test Cases
"""

from django.test import TestCase
from pprint import pprint
from app.models import Endpoint
from app.models import Namespace
from app.models import Request
from app.modules.entity.meta_entity import Meta_Entity
from django.contrib.auth.models import User
from app.modules.util.helpers import Helpers


class Test_Meta_Entity(TestCase):
	pass