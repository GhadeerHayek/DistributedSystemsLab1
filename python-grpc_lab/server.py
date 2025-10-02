import grpc
from concurrent import futures
import user_service_pb2
import user_service_pb2_grpc


class UserService(user_service_pb2_grpc.UserServiceServicer):
    users = {
        "1": user_service_pb2.User(id="1", name="John Doe", email=""),
    }

    def getUser(self, request, context):
        print("called the implementation of get user")
        # Implement GetUser
        # get the id
        user_id = request.id
        # check if the id exists in the users
        if user_id in self.users:
            # it's okay to use return as we have the customer's request
            return self.users[user_id]
        else:
            # we need to use the context to send back an error message
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"User with ID '{user_id}' not found.")
            return user_service_pb2.User(id=user_id, name="", email="")

    def updateUser(self, request, context):
        # implement UpdateUser
        # get the id, name, email
        user_id = request.id
        user_name = request.name
        user_email = request.email
        # TODO: should we check if the request should contain the three parameters?
        # TODO: or maybe it will fail if it does not follow gRPC specifications
        # if id is not in the list of keys .. return error
        if user_id not in self.users:
            # we need to use the context to send back an error message
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"User with ID '{user_id}' not found.")
            return user_service_pb2.User(id=user_id, name="", email="")
        else:
            self.users[user_id].name = user_name
            self.users[user_id].email = user_email
            return user_service_pb2.User(id=user_id, name=self.users[user_id].name, email=self.users[user_id].email)

    def deleteUser(self, request, context):
        # the request will contain the id of the user to delete
        id = request.id
        if id not in self.users:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"User with ID '{id}' not found.")
            return
        else:
            del self.users[id]
            return user_service_pb2.DeleteUserResponse(message=f"User with ID '{id}' deleted.")

    def createUser(self, request, context):
        # the request will contain the id, name, email of the user to create
        name = request.name
        email = request.email
        if name == "" or email == "":
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Name and email are required.")
            return user_service_pb2.User(id="", name="", email="")
        else:
            id = str(len(self.users) + 1)
            self.users[id] = user_service_pb2.User(id=id, name=name, email=email)
            return self.users[id]


# Implement other methods
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print("Starting server...")
    serve()
    print("Server stopped.")
