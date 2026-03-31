import json


def json_response(response : dict | list, status, start_response, response_header=None) -> list[bytes]:

    if response_header is None:
        response_header = []
    response = json.dumps(response)

    start_response(status,response_header)

    return [response.encode('utf-8')]






    


    