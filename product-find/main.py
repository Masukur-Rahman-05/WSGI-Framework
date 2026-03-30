from wsgiref.simple_server import make_server
from inventory import data
import json

def application(environ,start_response):

    path = environ['PATH_INFO']
    category = path.split("/")[-1]
    products = data.get(category,{})

    response_body = json.dumps(products)

    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
    ]

    start_response(status,response_headers)

    return [response_body.encode('utf-8')]

server = make_server('localhost',8000,app=application)
print("Server is listening to http://localhost:8000")
server.serve_forever()