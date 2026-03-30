# Exception Handler Example

This folder contains a small WSGI example that wraps an application with a custom exception-handling middleware.

The goal is to show how middleware can catch unhandled exceptions and return a structured JSON error response instead of crashing the request.

## File Structure

```text
exception-handler/
|-- main.py
|-- README.md
```

## Requirements

- Python 3.x

This example uses only Python's built-in `wsgiref.simple_server` and `json` modules.

## How to Run

From the project root:

```bash
python exception-handler/main.py
```

The server starts at:

```text
http://localhost:8000
```

## What `main.py` Does

`main.py` contains three main parts:

1. a small in-memory product dictionary
2. a helper function named `json_response()` for returning JSON responses
3. an `ExceptionHandler` middleware class that catches unhandled exceptions from the wrapped WSGI app

The application reads the request path, extracts the last path segment, and uses that segment as a lookup key in the `data` dictionary.

## Available Routes

### `GET /mobile`

Returns:

```json
{"mobile": {"product_id": 1, "product_name": "samsung", "price": "$1000"}}
```

Current implementation detail:

- the lookup key is `mobile`
- the returned JSON body is the product object for that category

Example response:

```json
{"product_id": 1, "product_name": "samsung", "price": "$1000"}
```

### `GET /laptop`

Example response:

```json
{"laptop_id": 1, "laptop_name": "Asus", "price": "$1500"}
```

### Unknown path

If the category does not exist, the application currently returns an empty JSON object:

```json
{}
```

## Exception Middleware

The `ExceptionHandler` class wraps the WSGI application:

```python
ExceptionHandler(application)
```

If the wrapped app raises an exception, the middleware catches it and returns:

- status: `500 Internal server error`
- content type: `application/json`
- body:

```json
{"message": "Unhandled Error has been occurred : <error message>"}
```

## How to Test the Error Handler

Inside `main.py`, there is a commented test line:

```python
# raise RuntimeError('Error for testing')
```

Uncomment it, restart the server, and make a request. The middleware will catch the exception and return a JSON `500` response.

## Learning Focus

This example demonstrates:

- how to build a WSGI middleware class
- how to wrap an application before passing it to the server
- how to catch unhandled exceptions centrally
- how to return JSON responses from a WSGI app

## Notes

- Stop the server with `Ctrl + C`
- This example is for learning; it does not yet include routing, status-specific error classes, or reusable response utilities
- A useful next step would be adding proper `404 Not Found` handling for unknown categories
