# Dynamic Routes Example

This folder contains a small WSGI application that moves routing into a reusable route manager instead of hard-coding path logic inside one function.

The example is still intentionally small, but it now demonstrates a cleaner structure for registering routes, dispatching requests, and wrapping the app with middleware.

## File Structure

```text
dynamic-routes/
|-- app.py
|-- common_handlers.py
|-- constants.py
|-- helpers.py
|-- middlewares.py
|-- product_controller.py
|-- router.py
|-- server.py
|-- README.md
```

## Requirements

- Python 3.x

This example uses only Python built-in modules.

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
- imports the wrapped middleware application from `app.py`
- imports `product_controller.py` so routes are registered before requests arrive

### `app.py`

- defines the `Application` class
- creates a `RouteManager` instance
- exposes the `@app.route(...)` decorator for route registration
- forwards incoming requests to `RouteManager.dispatch()`
- wraps the app with `ExceptionHandler`

### `router.py`

- contains the `RouteManager` class
- stores registered routes in a dictionary
- prevents duplicate route registration
- dispatches requests by matching `PATH_INFO`
- falls back to a 404 handler when no route matches

### `product_controller.py`

- registers the `/products` route with `@app.route("/products")`
- returns sample product data from `constants.py`

### `constants.py`

- stores the in-memory sample product data

### `helpers.py`

- contains `json_response()`
- converts Python dictionaries or lists into JSON bytes for WSGI responses

### `middlewares.py`

- contains the `ExceptionHandler` middleware class
- catches unhandled exceptions raised by the wrapped app

### `common_handlers.py`

- contains `Handler.generic_exception_handler()`
- contains `Handler.url_not_found_handler()`
- returns JSON responses for both `500` and `404` cases

## Current Request Flow

When a request comes in:

1. `server.py` starts the WSGI server with `middleware`
2. `ExceptionHandler` calls the wrapped `Application`
3. `Application.__call__()` forwards the request to `RouteManager.dispatch()`
4. `RouteManager` looks up the request path in its route table
5. the matched handler returns a JSON response
6. if no route matches, `Handler.url_not_found_handler()` returns a JSON `404`

If a registered handler raises an exception, the middleware catches it and returns a JSON `500` response instead.

## Available Routes

### `GET /products`

Response:

```json
{"product_id": 1, "product_name": "samsung", "price": "$1000"}
```

### `GET /anything-else`

If the path is not registered, the app returns:

```json
{"message": "Requested path /anything-else doesn't exist"}
```

Status:

```text
404 NOT FOUND
```

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

## Learning Focus

This example demonstrates:

- how to split a WSGI app across multiple modules
- how to register routes with a decorator
- how to dispatch requests with a small route manager
- how to return JSON from a WSGI application
- how to handle missing routes with a dedicated 404 handler
- how to wrap an application with exception-handling middleware

## Current Limitations

- route matching is exact string matching only
- there is no support for path parameters such as `/products/<id>`
- only one sample route is currently registered
- `product_controller.py` currently returns only the `mobile` product
- response headers are passed manually instead of through a response object

## Possible Next Steps

Natural next improvements for this example would be:

1. add support for dynamic path parameters
2. register separate handlers for multiple products or resources
3. introduce request and response classes
4. support method-based routing such as `GET` and `POST`
