from wsgiref.simple_server import make_server

def application(environ,start_response):

    response_body = [
        f"{key} : {value}" for key,value in sorted(environ.items())
    ]

    method = environ['REQUEST_METHOD']
    port = environ['SERVER_PORT']
    path = environ['PATH_INFO']

    print(method,port,path) # This is how we can extract the info from environ

    response_body = "\n".join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
    ]

    start_response(status,response_headers)

    return [response_body.encode('utf-8')]

server = make_server('localhost',8000,app=application)
print("Server is listening to http://localhost:8000")
server.serve_forever()