import unittest
from name_function import get_formatted_name

class TestCase(unittest.TestCase):
    '''test case for function get_formatted_name'''

    def test_name1(self):
        neatname = get_formatted_name('jack', 'gates')
        self.assertEqual(neatname, 'Jack Gates')
    def test_name2(self):
        neatname2= get_formatted_name(first='bill', middle='pil', last='gates')
        self.assertEqual(neatname2, 'Bill Pil Gates')
if __name__ == '__main__':

    unittest.main()
