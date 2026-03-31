from typing import Callable

class ExceptionHandler:
    def __init__(self,app,exception_handler:Callable):
        self.wrapped_app = app
        self.exception_handler = exception_handler

    def __call__(self,environ,start_response):
        try:
            return self.wrapped_app(environ,start_response)
        except Exception as e:
            return self.exception_handler(environ,start_response,exception=e)
            