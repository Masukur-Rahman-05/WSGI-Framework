from constants import data
from helpers import json_response
from common_handlers import Handler


class RouteManager:
    def __init__(self):
        self.routes = {}

    def register(self,path,handler):
        if path in self.routes:
            raise RuntimeError(f"Path {path} is already bind with another handler")
        self.routes[path] = handler

    def dispatch(self,environ,start_response):
        path = environ['PATH_INFO']
        handler = self.routes.get(path,Handler.url_not_found_handler)
        response = handler(environ,start_response)
        return response

        # category = path.split("/")[-1]
        # product = data.get(category,{})
        # status = '200 OK'
        # response_headers = [
        # ('Content-type','application/json')
        # ]

        # # Uncomment the next line to see the exception handling

        # # raise RuntimeError('Error for testing')
        # return json_response(response=product,status=status,start_response=start_response,response_header=response_headers)