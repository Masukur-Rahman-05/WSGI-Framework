from wsgiref.simple_server import make_server
from app import middleware


if __name__ == "__main__":

    server = make_server('localhost',8000,app=middleware)
    print('Server is listening on http://localhost:8000')
    server.serve_forever()