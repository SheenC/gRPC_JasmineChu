import grpc
from concurrent import futures
import library_pb2
import library_pb2_grpc


class LibraryService(library_pb2_grpc.InventoryServiceServicer):

    # Store the (id, inventory) pair into a dict
    inventories = dict()


    def __init__(self, *args, **kwargs):
        # Store some books in the inventories
        book_1 = library_pb2.Book(ISBN="ISBN0011", title="Book One", author="Lucy", genre=["genre1", "genre2"], year=2012)
        book_2 = library_pb2.Book(ISBN="ISBN0012", title="Book Two", author="Jennie", genre=["genre1"], year=1982)
        book_3 = library_pb2.Book(ISBN="ISBN0013", title="Book Three", author="Ann", genre=["genre1", "genre3"], year=2005)
        inventory_1 = library_pb2.InventoryItem(id=book_1.ISBN, book=book_1, status=library_pb2.InventoryItem.Status.AVAILABLE)
        inventory_2 = library_pb2.InventoryItem(id=book_2.ISBN, book=book_2, status=library_pb2.InventoryItem.Status.TAKEN)
        inventory_3 = library_pb2.InventoryItem(id=book_3.ISBN, book=book_3, status=library_pb2.InventoryItem.Status.AVAILABLE)
        LibraryService.inventories[inventory_1.id] = inventory_1
        LibraryService.inventories[inventory_2.id] = inventory_2
        LibraryService.inventories[inventory_3.id] = inventory_3

    def CreateBook(self, request, context):
        # Print hint message on the server side
        print("Creating a new book ... \n")

        # Create a new inventory object
        inventory = library_pb2.InventoryItem(id=request.id, book=request.book, status=request.status)

        # Store the (id, inventory) pair into the dict
        LibraryService.inventories[request.id] = inventory

        # Print all (id, inventory) pair on the server side
        print("The inventories: \n", LibraryService.inventories)

        # Return response message
        return library_pb2.BookCreateResponse(message="The book inventory is created successfully! \n")
    

    def GetBook(self, request, context):
        # Print hint message on the server side
        print("Finding book with ISBN: " + request.ISBN + " ... \n")

        # Search the inventory in the dict using ISBN as its id 
        get_book_result = LibraryService.inventories.get(request.ISBN)

        # Create response message according to the search result
        if (get_book_result == None):
            result = "The book " + request.ISBN + " is not found! \n"
        else:
            result = "The book " + request.ISBN + " is found successfully! The result is: \n" + str(get_book_result)
        
        # Print finding result on the server side
        print(result)

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