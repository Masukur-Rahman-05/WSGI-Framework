# Exception Handler Example

This folder shows a small WSGI application wrapped by custom exception-handling middleware.

The example focuses on one idea: if the app raises an unhandled exception, the middleware catches it and returns a JSON `500` response instead of letting the request fail silently.

## File Structure

```text
exception-handler/
|-- main.py
|-- README.md
```

## Requirements

- Python 3.x

This example uses only built-in modules:

- `wsgiref.simple_server`
- `json`
- `typing`

## How to Run

From the project root:

```bash
python exception-handler/main.py
```

The server starts on:

```text
http://localhost:8000
```

## What `main.py` Contains

`main.py` is organized into four parts:

1. `data`: a simple in-memory product store
2. `json_response()`: a helper for JSON WSGI responses
3. `Handler.generic_exception_handler()`: a reusable exception response function
4. `ExceptionHandler`: middleware that wraps the application and catches errors

The `application()` function reads `PATH_INFO`, extracts the last path segment, and uses it as a key in the `data` dictionary.

## Available Routes

### `GET /mobile`

Response:

```json
{"product_id": 1, "product_name": "samsung", "price": "$1000"}
```

### `GET /laptop`

Response:

```json
{"laptop_id": 1, "laptop_name": "Asus", "price": "$1500"}
```

### `GET /anything-else`

If the key does not exist in `data`, the app currently returns an empty JSON object:

```json
{}
```

This is still a `200 OK` response in the current implementation.

## Exception Handling Flow

The application is wrapped like this:

```python
wrapped_app = ExceptionHandler(
    app=application,
    exception_handler=Handler.generic_exception_handler
)
```

When the wrapped app raises an exception:

1. `ExceptionHandler.__call__()` catches it
2. the middleware forwards the exception to `Handler.generic_exception_handler()`
3. the handler returns a JSON error response

The error response is:

- status: `500 Internal server error`
- content type: `application/json`
- body:

```json
{"message": "Unhandled Error has been occurred : <error message>"}
```

## How to Test the Middleware

In `main.py`, this test line is currently commented out:

```python
# raise RuntimeError('Error for testing')
```

To test the middleware:

1. uncomment that line
2. restart the server
3. send a request to any route

You should receive a JSON `500` response from the exception handler.

## Learning Focus

This example demonstrates:

- how to build custom WSGI middleware
- how to wrap a WSGI application before serving it
- how to centralize exception handling
- how to return JSON responses from both normal and error paths

## Current Limitations

- unknown routes return `{}` with `200 OK` instead of `404 Not Found`
- response headers only include `Content-type`
- the error message text is hard-coded
- the sample data uses different key names for `mobile` and `laptop`

## Possible Next Step

A practical next improvement would be returning a proper `404 Not Found` response for missing categories.
