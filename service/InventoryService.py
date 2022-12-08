import grpc
from concurrent import futures
import library_pb2
import library_pb2_grpc


class LibraryService(library_pb2_grpc.InventoryServiceServicer):

    # Store the (id, inventory) pair into a dict
    inventories = dict()

    def __init__(self, *args, **kwargs):
        pass

    def CreateBook(self, request, context):
        # Create a new inventory object
        inventory = library_pb2.InventoryItem(id=request.id, book=request.book, status=request.status)
        # Store the (id, inventory) pair into the dict
        LibraryService.inventories[request.id] = inventory
        # Print all (id, inventory) pair on the server side
        print("The inventories: \n", LibraryService.inventories)
        # Return response message
        return library_pb2.BookCreateResponse(message="The book inventory is created successfully! \n")
    
    def GetBook(self, request, context):
        # Search the inventory in the dict using ISBN as its id 
        get_book_result = LibraryService.inventories.get(request.ISBN)

        # Create response message according to the search result
        if (get_book_result == None):
            result = "The book " + request.ISBN + " is not found! \n"
        else:
            result = "The book " + request.ISBN + " is found successfully! The result is: \n" + str(get_book_result)
        
        # Return response message
        return library_pb2.BookGetResponse(message=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_InventoryServiceServicer_to_server(LibraryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC starting")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()