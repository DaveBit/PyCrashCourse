import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Test for 'test_name_function.py'"""
    def test_city_country(self):
        formatted_name = city_country('valencia', 'spain')
        self.assertEqual(formatted_name, 'Valencia, Spain')

unittest.main