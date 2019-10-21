greeter
=======

This is a simple implementation of the greeting API in https://github.com/brymck/schemas

Usage
-----

Install requirements:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python server.py
```

Send a request via the client:

```bash
python client.py
```

or via something like [`uber/prototool`](https://github.com/uber/prototool) while in the `brymck/schemas` project directory:

```bash
prototool grpc proto \
  --address localhost:50051 \
  --method brymck.greeting.v1.GreetingAPI/Greet \
  --data '{"person": {"first_name": "John", "last_name": "Smith"}, "language": "LANGUAGE_ENGLISH"}'
```
