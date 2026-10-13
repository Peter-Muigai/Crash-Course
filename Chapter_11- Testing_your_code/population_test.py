import unittest
from population import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for population.py."""

    def test_city_country_population(self):
        """Does city, country and population work?"""
        formatted_city = city_country('nairobi', 'kenya', 1000000)
        self.assertEqual(formatted_city, 'Nairobi, Kenya- 1000000')

if __name__ == '__main__':
    unittest.main()