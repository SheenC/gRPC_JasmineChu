import grpc
from concurrent import futures
import library_pb2
import library_pb2_grpc


class LibraryService(library_pb2_grpc.InventoryServiceServicer):

    dict = {}

    def __init__(self, *args, **kwargs):
        pass

    def CreateBook(self, request, context):
        book_1 = library_pb2.BOOK(ISBN=request.ISBN)
        book_1.title = request.title
        book_1.author = request.author
        book_1.genre = request.genre
        book_1.year = request.year

        book_1_type = library_pb2.OneOfType(type_oneof=book_1)
        inventory_1 = library_pb2.InventoryItem(id=request.ISBN)
        inventory_1.type = book_1_type
        inventory_1.status = library_pb2.InventoryItem.Status.AVAILABLE

        dict.add(inventory_1.id, inventory_1)

        result = "The book is created successfully!"
        return library_pb2.BookCreateResponse(**result)
    
    def GetBook(self, request, context):
        book_found = dict.get(request.ISBN)
        return library_pb2.BookGetResponse(message="The book is found!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_InventoryServiceServicer_to_server(LibraryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()