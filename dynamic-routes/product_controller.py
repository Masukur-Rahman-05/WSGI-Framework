from app import app
from constants import data
from helpers import json_response



@app.route("/products")
def get_products(environ,start_response):
    response = data.get("mobile")
    return json_response(response=response,status="200 OK",start_response=start_response,response_header=[])