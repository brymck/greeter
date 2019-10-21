import grpc

from brymck.greeting.v1.greeting_api_pb2 import GreetRequest, GreetResponse
from brymck.greeting.v1.greeting_api_pb2_grpc import GreetingAPIStub
from brymck.language.v1.language_pb2 import LANGUAGE_ENGLISH
from brymck.person.v1.person_pb2 import Person


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = GreetingAPIStub(channel)
        person = Person(first_name='Bryan', last_name='McKelvey')
        request = GreetRequest(person=person, language=LANGUAGE_ENGLISH)
        print('Sending request:')
        print(request)
        response = stub.Greet(request)
    print('Received response:')
    print(response)


if __name__ == '__main__':
    run()
