import os, sys
sys.path.insert(0, os.path.abspath("."))
import requests_mock
import unittest
from inventory_client import InventoryClient
from get_book_titles import GetBookTitles

class TestAPI(unittest.TestCase):

    @requests_mock.mock()
    def test_getBookName(self, m):
        a = InventoryClient()
        m.get('ISBN0001', text='ISBN0001')
        self.assertEqual(a.getBookName('ISBN0001'), 'My Book')
        m.get('ISBN0001', text='ISBN0011')
        self.assertEqual(a.getBookName('ISBN0011'), 'Book One')
        m.get('ISBN0001', text='ISBN0012')
        self.assertEqual(a.getBookName('ISBN0012'), 'Book Two')

if __name__ == '__main__':
    unittest.main()