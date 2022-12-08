import grpc
import sys
# adding service to the system path
sys.path.insert(0, '../service')
from service import library_pb2_grpc as pb2_grpc
from service import library_pb2 as pb2


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
        self.stub = pb2_grpc.InventoryServiceStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = InventoryClient()
    result = client.get_url(message="Hello Server you there?")
    print(f'{result}')