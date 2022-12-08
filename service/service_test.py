import grpc

import library_pb2
import library_pb2_grpc

def run():
   with grpc.insecure_channel('localhost:50051') as channel:
      stub = library_pb2_grpc.InventoryServiceStub(channel)

      book = library_pb2.Book(ISBN="ISBN0001", title="My Book", author="Jasmine", genre=["happy","great"], year=2022)
      bookCreateRequest = library_pb2.BookCreateRequest(id=book.ISBN, book=book, status=library_pb2.InventoryItem.Status.AVAILABLE)
      bookCreateResponse = stub.CreateBook(bookCreateRequest)
      print("Inventory client received following from server: " + bookCreateResponse.message)  

      bookGetRequest = library_pb2.BookGetRequest(ISBN="ISBN0001")
      bookGetResponse = stub.GetBook(bookGetRequest)
      print("Inventory client received following from server: " + bookGetResponse.message)  

      bookGetRequest_not_found = library_pb2.BookGetRequest(ISBN="ISBN9999")
      bookGetResponse_not_found = stub.GetBook(bookGetRequest_not_found)
      print("Inventory client received following from server: " + bookGetResponse_not_found.message)  
run()