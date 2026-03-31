# Dynamic Routes Example

This folder contains a small WSGI application split into multiple modules to make route handling and middleware easier to extend.

The current implementation still uses the last URL path segment as a lookup key, but the structure is closer to a reusable app layout than the earlier single-file examples.

## File Structure

```text
dynamic-routes/
|-- app.py
|-- common_handlers.py
|-- constants.py
|-- helpers.py
|-- middlewares.py
|-- server.py
|-- README.md
```

## Requirements

- Python 3.x

This example uses only built-in Python modules.

## How to Run

From the project root:

```bash
python dynamic-routes/server.py
```

The server starts on:

```text
http://localhost:8000
```

## What Each File Does

### `server.py`

- starts the WSGI server with `wsgiref.simple_server`
- imports the wrapped application from `app.py`

### `app.py`

- defines the `Application` class
- reads the request path from `PATH_INFO`
- extracts the last path segment as a category
- looks up product data from `constants.py`
- returns a JSON response
- wraps the app with `ExceptionHandler`

### `constants.py`

- stores the in-memory sample product data

### `helpers.py`

- contains `json_response()`
- converts Python dictionaries or lists into JSON bytes for WSGI responses

### `middlewares.py`

- contains the `ExceptionHandler` middleware class
- catches unhandled exceptions from the wrapped app

### `common_handlers.py`

- contains `Handler.generic_exception_handler()`
- returns a JSON `500` response when an exception occurs

## Current Request Flow

When a request comes in:

1. `server.py` serves the wrapped middleware app
2. `ExceptionHandler` calls the `Application` instance
3. `Application` reads `PATH_INFO`
4. the last path segment is used as a lookup key in `data`
5. the result is returned through `json_response()`

If an exception is raised, the middleware catches it and returns a JSON error response instead.

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

If the key does not exist, the app currently returns:

```json
{}
```

This is still returned with `200 OK`.

## Exception Handling

The application is wrapped like this in `app.py`:

```python
middleware = ExceptionHandler(
    app=app,
    exception_handler=Handler.generic_exception_handler
)
```

If the wrapped app raises an exception, the response is:

- status: `500 Internal server error`
- content type: `application/json`
- body:

```json
{"message": "Unhandled Error has been occurred : <error message>"}
```

## How to Test the Error Handler

In `app.py`, this line is available for testing:

```python
# raise RuntimeError('Error for testing')
```

To test exception handling:

1. uncomment that line
2. restart the server
3. send a request to any route

## Learning Focus

This example demonstrates:

- how to split a WSGI app across multiple files
- how to organize helpers, constants, middleware, and handlers
- how to return JSON from a WSGI application
- how to wrap a class-based application with middleware
- how to centralize exception handling

## Current Limitations

- route matching is still based only on the last path segment
- there is no real dynamic parameter parsing yet
- unknown routes return `{}` instead of `404 Not Found`
- sample data keys are not standardized between products

## Possible Next Step

A strong next step would be adding real dynamic route patterns such as `/products/<category>` or `/products/<category>/<id>`.
