from concurrent import futures

import grpc

from brymck.greeting.v1.greeting_api_pb2 import GreetRequest, GreetResponse
from brymck.greeting.v1.greeting_api_pb2_grpc import GreetingAPIServicer, add_GreetingAPIServicer_to_server


class GreetingAPIServicerImpl(GreetingAPIServicer):
    def Greet(self, request: GreetRequest, context):
        print('Received request:')
        print(request)
        message = 'Hello, {}!'.format(request.person.first_name)
        response = GreetResponse(message=message)
        print('Sending response:')
        print(response)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreetingAPIServicer_to_server(GreetingAPIServicerImpl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('gRPC server started on localhost:50051')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
