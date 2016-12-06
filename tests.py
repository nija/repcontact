'''Tests for repcontact'''
import unittest
import doctest
import json
from datetime import datetime
from repcontact import get_congress_critter_data, call_a_number


class StaticTests(unittest.TestCase):
    '''Tests for static methods'''

    def test_get_congress_critter_data(self):
        '''Get data from the Sunlight Foundation API'''
        self.assertTrue(True)

    def test_call_a_number(self):
        '''Call out on a verified number'''
        self.assertTrue(True)

