from concurrent import futures
import grpc

import os

os.path.join(os.path.dirname(__file__), 'pb')

import pb.hello_world_pb2 as hello_world_pb2
import pb.hello_world_pb2_grpc as hello_world_pb2_grpc

# レスポンスの処理
class Greeter(hello_world_pb2_grpc.HelloWorldServiceServicer):
    def SayHello(self, request, context):
        return hello_world_pb2.HelloWorldResponse(message="hello world")

# サーバー起動処理
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_world_pb2_grpc.add_HelloWorldServiceServicer_to_server(Greeter(), server)
    
    # サーバー起動
    server.add_insecure_port('[::]:5001')
    server.start()
    print("server sstarted")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()