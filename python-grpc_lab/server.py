import grpc
from concurrent import futures
import user_service_pb2
import user_service_pb2_grpc


class UserService(user_service_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
    # Implement GetUser
        pass


# Implement other methods
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()