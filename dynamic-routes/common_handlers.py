from helpers import json_response

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
    
    @staticmethod
    def url_not_found_handler(environ,start_response):

        response_headers = [
            ('Content-type','application/json')
        ]

        path = environ.get("PATH_INFO")

        response = {
            "message":f"Requested path {path} doesn't exist"
        }

        return json_response(response=response,start_response=start_response,status='404 NOT FOUND',response_header=response_headers)