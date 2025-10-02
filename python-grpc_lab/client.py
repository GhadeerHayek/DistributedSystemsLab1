import grpc
from generated import user_service_pb2
from generated import user_service_pb2_grpc

# connection on the same port of the server
channel = grpc.insecure_channel('localhost:50051')

# client stub object is imported from the grpc generated file
stub = user_service_pb2_grpc.UserServiceStub(channel)
# call to get user service, but pass a get user request object, which is generated from the proto file
# also you should notice that by definition:
# the get user request is made up from the id field, and it comes as the first one or it has a tag with number one

get_user_response = stub.getUser(user_service_pb2.GetUserRequest(id="1"))
print("Get user response: ", get_user_response)
create_user_response = stub.createUser(user_service_pb2.CreateUserRequest(name="Ghadeer Test", email="ghadeerhayek@gmail.com"))
print("Create user response: ", create_user_response)
update_user_response = stub.updateUser(user_service_pb2.UpdateUserRequest(id="1", name="previous example", email="emailremainsthesame"))
print("Update user response: ", update_user_response)
delete_user_response = stub.deleteUser(user_service_pb2.DeleteUserRequest(id="1"))
print("Delete user response: ", delete_user_response)