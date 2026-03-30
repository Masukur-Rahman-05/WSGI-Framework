from wsgiref.simple_server import make_server

class reverseware:
    def __init__(self,app):
        self.wrapped_application = app

    def __call__(self,environ,start_response,*args,**kwargs):
        wrapped_app_response = self.wrapped_application(environ,start_response)

        return [data[::-1] for data in wrapped_app_response]
    
def application(environ,start_response):

    response_body = "Hello World"

    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain')
    ]
    start_response(status,response_headers)

    return [response_body.encode('utf-8')]

server = make_server('localhost',8000,app=reverseware(application))
print("Server is listening on http://localhost:8000")
server.serve_forever()