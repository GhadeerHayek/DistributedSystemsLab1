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
        pass

    def deleteUser(self, request, context):

        pass

    def createUser(self, request, context):
        pass


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