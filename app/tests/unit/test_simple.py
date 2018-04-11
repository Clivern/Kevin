"""
Simple Test Case
"""

from django.test import TestCase


class TestSimple(TestCase):

    def test_method(self):
        self.assertEqual('The lion says "roar"', 'The lion says "roar"')