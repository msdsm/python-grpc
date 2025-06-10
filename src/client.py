import grpc
from pb import hello_world_pb2
from pb import hello_world_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:5001') as channel:
        stub = hello_world_pb2_grpc.HelloWroldServiceStub(channel)
        response = stub.SayHello(hello_world_pb2.HelloWorldRequest())
    print(f"Response: {response.message}")

if __name__ == '__main__':
    run()