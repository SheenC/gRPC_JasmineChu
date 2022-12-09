import os, sys
sys.path.insert(0, os.path.abspath("."))
from inventory_client import InventoryClient

class GetBookTitles(object):
    """
    Given a list of ISBN, return a list of book names
    """

    def __init__(self):
        self.client = InventoryClient()

    def getBookNames(self, ISBNs):
        names = []
        for isbn in ISBNs:
            name = self.client.getBookName(ISBN=isbn)
            names.append(name)
            
        return names


if __name__ == '__main__':
    getBookTitles = GetBookTitles()
    result = getBookTitles.getBookNames(ISBNs=["ISBN0001","ISBN0011"])
    print("The name is: ", result)

