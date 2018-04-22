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


	def test_insert_one(self):
        pass

	def test_insert_many(self):
		pass

	def test_get_one_by_id(self):
		pass

	def test_get_one_by_item_id_key(self):
		pass

	def test_get_many_by_key(self):
		pass

	def test_get_many_by_item_id(self):
		pass

	def test_update_one_by_id(self):
		pass

	def test_update_one_by_item_id_key(self):
		pass

	def test_delete_one_by_id(self):
		pass

	def test_delete_one_by_item_id_key(self):
		pass