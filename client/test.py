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
        self.mockClient.getBookName = MagicMock(return_value = 'The other book')

# Test inventory_client
class TestInventoryClient(unittest.TestCase):
    @patch('inventory_client.InventoryClient.getBookName')
    def testInventoryClient(self, mock_getBookName):
        mockClient = MockClient().mockClient
        self.assertEqual(mockClient.getBookName(ISBN='ISBN6789', key='value'), 'The other book')

# Test get_book_titles
class TestGetBookTitles(unittest.TestCase):
    @patch('get_book_titles.GetBookTitles.getBookNames')
    def testGetBookTitles(self, mock_getBookTitles):
        getBookTitles = GetBookTitles(MockClient)
        getBookTitles.getBookNames = MagicMock(return_value = ['The other book','The anotther book'])
        self.assertEqual(getBookTitles.getBookNames(ISBNs=['ISBN6789','ISBN5678'], key='value'), ['The other book', 'The anotther book'])


if __name__ == '__main__':
    unittest.main()
    