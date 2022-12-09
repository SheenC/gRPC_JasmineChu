import grpc
import os, sys
sys.path.insert(0, os.path.abspath("."))
import library_pb2
import library_pb2_grpc
import re


class InventoryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = library_pb2_grpc.InventoryServiceStub(self.channel)

    def getBookName(self, ISBN):
        """
        Client function to call the rpc for BookGet Service
        """
        # Search book by its ISBN
        bookGetRequest = library_pb2.BookGetRequest(ISBN=ISBN)
        # Get the response in a string 
        bookGetResponse = self.stub.GetBook(bookGetRequest)
        # use regex to extract the book name
        name = re.search('title(.*)author', str(bookGetResponse)).group(1)
        # remove the quote and special symbols around the book name
        name = name[4 : len(name)-6]
        # Print info in client side
        print("Inventory client received following from server: " + bookGetResponse.message) 
        # return the book name 
        return name


if __name__ == '__main__':
    client = InventoryClient()
    result = client.getBookName(ISBN="ISBN0001")
    print("The name is: ", result)
