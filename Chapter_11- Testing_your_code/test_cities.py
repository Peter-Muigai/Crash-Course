import unittest
from city_function import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for city_function.py."""

    def test_city_country(self):
        """Does city, country work?"""
        formatted_city = city_country('nairobi', 'kenya')
        self.assertEqual(formatted_city, 'Nairobi, Kenya')

if __name__ == '__main__':
    unittest.main()