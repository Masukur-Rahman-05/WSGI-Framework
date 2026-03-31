from wsgiref.simple_server import make_server
import json
from typing import Callable

data = {
    "mobile":{
        "product_id":1,
        "product_name": "samsung",
        "price":"$1000"
    },
    "laptop":{
        "laptop_id":1,
        "laptop_name" : "Asus",
        "price":"$1500"
    }
}



def json_response(response : dict | list, status, start_response, response_header=None) -> list[bytes]:

    if response_header is None:
        response_header = []
    response = json.dumps(response)

    start_response(status,response_header)

    return [response.encode('utf-8')]


class Handler:
    @staticmethod
    def generic_exception_handler(environ,start_response, exception:Exception)->list[bytes]:
        response_headers = [
            ('Content-type','application/json')
        ]
            
        response = {
                "message":f"Unhandled Error has been occurred : {exception}"
        }
        return json_response(response=response,status='500 Internal server error',start_response=start_response,response_header=response_headers)



    
class ExceptionHandler:
    def __init__(self,app,exception_handler:Callable):
        self.wrapped_app = app
        self.exception_handler = exception_handler

    def __call__(self,environ,start_response):
        try:
            return self.wrapped_app(environ,start_response)
        except Exception as e:
            return self.exception_handler(environ,start_response,exception=e)
            


def application(environ, start_response):

    path = environ['PATH_INFO']
    category = path.split("/")[-1]
    product = data.get(category,{})

    status = '200 OK'
    response_headers = [
        ('Content-type','application/json')
    ]

    # Uncomment the next line to see the exception handling

    # raise RuntimeError('Error for testing')
    return json_response(response=product,status=status,start_response=start_response,response_header=response_headers)


if __name__ == "__main__":

    wrapped_app = ExceptionHandler(
        app = application,
        exception_handler=Handler.generic_exception_handler
    )
    server = make_server('localhost',8000,app=wrapped_app)
    print('Server is listening on http://localhost:8000')
    server.serve_forever()

    

