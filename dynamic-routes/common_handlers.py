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