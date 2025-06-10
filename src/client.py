import grpc

import os

os.path.join(os.path.dirname(__file__), 'pb')

import pb.hello_world_pb2 as hello_world_pb2
import pb.hello_world_pb2_grpc as hello_world_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:5001') as channel:
        stub = hello_world_pb2_grpc.HelloWorldServiceStub(channel)
        response = stub.SayHello(hello_world_pb2.HelloWorldRequest())
    print(f"Response: {response.message}")

if __name__ == '__main__':
    run()