# A passing test
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py."""

    def test_first_last_name(self):
        """Do names with first and last work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last(self):
        """Do names with first, middle and last work?"""
        formatted_name = get_formatted_name('simon', 'mwangi', 'peter'
                                            )
        self.assertEqual(formatted_name, 'Simon Peter Mwangi')

if __name__ == '__main__':
    unittest.main()