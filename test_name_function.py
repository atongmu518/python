import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        full_name = get_formatted_name('jerRy', 'ZHU')

        self.assertEqual(full_name, 'Jerry Zhu')

unittest.main()
