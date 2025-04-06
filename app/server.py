import grpc
from concurrent.futures import ThreadPoolExecutor
import goodbye_pb2
import goodbye_pb2_grpc

class Farewell(goodbye_pb2_grpc.FarewellServicer):
    def SayGoodbye(self, request, context):
        return goodbye_pb2.GoodbyeReply(message=f"Goodbye, {request.name} from gRPC!")

def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    goodbye_pb2_grpc.add_FarewellServicer_to_server(Farewell(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
