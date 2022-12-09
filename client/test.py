import os, sys
sys.path.insert(0, os.path.abspath("."))
import unittest
from inventory_client import InventoryClient
from get_book_titles import GetBookTitles
from unittest.mock import MagicMock, patch

# Create a mock of the API class interface defined at inventory_client
class MockInventoryClient(object):

    def __init__(self):

        def side_effect_func(ISBN):
            ISBN_title_dict = {'ISBN0011': 'Book One', 'ISBN0012': 'Book Two', 'ISBN0013': 'Book Three'}
            if ISBN in ISBN_title_dict.keys():
                return ISBN_title_dict[ISBN]
            else:
                return '[Not Found]'

        self.mockClient = InventoryClient()
        self.mockClient.getBookName = MagicMock(side_effect=side_effect_func)


# Create a mock API of get_book_titles
class MockGetBookTitles(object):

    def __init__(self):

        def side_effect_func(ISBNs):
            ISBN_title_dict = {'ISBN0011': 'Book One', 'ISBN0012': 'Book Two', 'ISBN0013': 'Book Three'}
            titles = []
            for ISBN in ISBNs:
                
                if ISBN in ISBN_title_dict.keys():
                    titles.append(ISBN_title_dict[ISBN])
                else:
                    titles.append('[Not Found]')
            return titles

        self.mockClient = GetBookTitles()
        self.mockClient.getBookNames = MagicMock(side_effect=side_effect_func)
 

# Test inventory_client with a mock client
class TestInventoryClient(unittest.TestCase):
    @patch('inventory_client.InventoryClient.getBookName')
    def testInventoryClient(self, mock_getBookName):
        mockClient = MockInventoryClient().mockClient
        self.assertEqual(mockClient.getBookName('ISBN0011'), 'Book One')
        self.assertEqual(mockClient.getBookName('ISBN0012'), 'Book Two')
        self.assertEqual(mockClient.getBookName('ISBN0013'), 'Book Three')
        self.assertEqual(mockClient.getBookName('ISBN6789'), '[Not Found]')


# Test get_book_titles with a mock client
class TestGetBookTitles(unittest.TestCase):
    @patch('get_book_titles.GetBookTitles.getBookNames')
    def testGetBookTitles(self, mock_getBookTitles):
        getBookTitles = MockGetBookTitles().mockClient
        self.assertEqual(getBookTitles.getBookNames(['ISBN0011','ISBN0012', 'ISBN6789']), ['Book One', 'Book Two', '[Not Found]'])


# Test inventory_client with a live server
class TestInventoryClientWithServerOn(unittest.TestCase):
    def testInventoryClient(self):
        client = InventoryClient()
        self.assertEqual(client.getBookName(ISBN='ISBN0011'), 'Book One')
        self.assertEqual(client.getBookName(ISBN='ISBN0012'), 'Book Two')
        self.assertEqual(client.getBookName(ISBN='ISBN0013'), 'Book Three')
        self.assertEqual(client.getBookName(ISBN='ISBN6789'), '[Not Found]')


# Test get_book_titles with a live server
class TestGetBookTitlesWithServerOn(unittest.TestCase):
    def testGetBookTitles(self):
        client = GetBookTitles()
        self.assertEqual(client.getBookNames(ISBNs=['ISBN0011', 'ISBN6789']), ['Book One', '[Not Found]'])


if __name__ == '__main__':
    unittest.main()
    