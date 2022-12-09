import os, sys
sys.path.insert(0, os.path.abspath("."))
import unittest
from inventory_client import InventoryClient
from get_book_titles import GetBookTitles
from unittest.mock import MagicMock, patch

# Create a mock of the API class interface defined at inventory_client
class MockClient(object):

    def __init__(self):
        pass
        self.mockClient = InventoryClient()
        self.mockClient.getBookName = MagicMock(request="", return_value = 'The other book')

# Test inventory_client without starting server
class TestInventoryClient(unittest.TestCase):
    @patch('inventory_client.InventoryClient.getBookName')
    def testInventoryClient(self, mock_getBookName):
        mockClient = MockClient().mockClient
        self.assertEqual(mockClient.getBookName(ISBN='ISBN6789', key='value'), 'The other book')

# Test get_book_titles without starting server
class TestGetBookTitles(unittest.TestCase):
    @patch('get_book_titles.GetBookTitles.getBookNames')
    def testGetBookTitles(self, mock_getBookTitles):
        getBookTitles = GetBookTitles()
        getBookTitles.getBookNames = MagicMock(return_value = ['The other book','The anotther book'])
        self.assertEqual(getBookTitles.getBookNames(ISBNs=['ISBN6789','ISBN5678'], key='value'), ['The other book', 'The anotther book'])

# Test inventory_client starting server
class TestInventoryClientWithServerOn(unittest.TestCase):
    def testInventoryClient(self):
        client = InventoryClient()
        self.assertEqual(client.getBookName(ISBN='ISBN0011'), 'Book One')
        self.assertEqual(client.getBookName(ISBN='ISBN6789'), '[Not Found]')

# Test get_book_titles starting server
class TestGetBookTitlesWithServerOn(unittest.TestCase):
    def testGetBookTitles(self):
        client = GetBookTitles()
        self.assertEqual(client.getBookNames(ISBNs=['ISBN0011', 'ISBN6789']), ['Book One', '[Not Found]'])

if __name__ == '__main__':
    unittest.main()
    