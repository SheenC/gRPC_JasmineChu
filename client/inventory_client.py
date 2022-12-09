import grpc
import os, sys
sys.path.insert(0, os.path.abspath("."))
import library_pb2
import library_pb2_grpc
import service.InventoryService
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
        Client function to call the rpc for GetServerResponse
        """
        bookGetRequest = library_pb2.BookGetRequest(ISBN=ISBN)
        bookGetResponse = self.stub.GetBook(bookGetRequest)
        name = re.search('title(.*)author', str(bookGetResponse)).group(1)
        name = name[4 : len(name)-6]
        print("Inventory client received following from server: " + bookGetResponse.message)  
        return name


if __name__ == '__main__':
    client = InventoryClient()
    result = client.getBookName(ISBN="ISBN0001")
    print("The name is: ", result)
