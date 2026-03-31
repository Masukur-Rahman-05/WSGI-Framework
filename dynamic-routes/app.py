from constants import data
from helpers import json_response
from middlewares import ExceptionHandler
from common_handlers import Handler


class Application:

    def __init__(self):
        pass

    def __call__(self,environ,start_response):
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

# def application(environ, start_response):

#     path = environ['PATH_INFO']
#     category = path.split("/")[-1]
#     product = data.get(category,{})

#     status = '200 OK'
#     response_headers = [
#         ('Content-type','application/json')
#     ]

#     # Uncomment the next line to see the exception handling

#     # raise RuntimeError('Error for testing')
#     return json_response(response=product,status=status,start_response=start_response,response_header=response_headers)

app = Application()
middleware = ExceptionHandler(
    app = application,
    exception_handler=Handler.generic_exception_handler
)
