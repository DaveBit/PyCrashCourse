import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Test for 'test_name_function.py'"""
    def test_city_country(self):
        formatted_name = city_country('valencia', 'spain')
        self.assertEqual(formatted_name, 'Valencia, Spain')

    def test_city_country_population(self):
        formatted_name = city_country('santiago', 'chile', population=500000)
        self.assertEqual(formatted_name, 'Santiago, Chile - Population 500000')

unittest.main
