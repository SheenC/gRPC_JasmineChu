import grpc
import os, sys
sys.path.insert(0, os.path.abspath("."))
import library_pb2
import library_pb2_grpc
import service.InventoryService


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

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = library_pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = InventoryClient()
    result = client.get_url(message="Hello Server you there?")
    print(f'{result}')