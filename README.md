# WSGI Web Framework

This repository is a small learning project for understanding how Python WSGI applications and middleware work.

The codebase is organized as a collection of simple, focused examples. Each example runs independently and demonstrates one part of building a lightweight web framework with WSGI.

## Project Structure

```text
WSGI Web Framework/
|-- main.py
|-- reverseware.py
|-- README.md
|-- product-find/
|   |-- inventory.py
|   |-- main.py
|   |-- README.md
|-- exception-handler/
|   |-- main.py
|   |-- README.md
```

## Requirements

- Python 3.x

This project uses only Python built-in modules, mainly:

- `wsgiref.simple_server`
- `json`
- `typing`

No external packages are required.

## How to Run

Each example starts its own local server on:

```text
http://localhost:8000
```

Run only one example at a time because they all use the same port.

From the project root, you can run:

```bash
python main.py
python reverseware.py
python product-find/main.py
python exception-handler/main.py
```

Stop the server with `Ctrl + C`.

## Examples Overview

### 1. `main.py`

This is the most basic WSGI example in the project.

It demonstrates the standard WSGI application signature:

```python
application(environ, start_response)
```

Current behavior:

- reads the WSGI `environ` dictionary
- extracts `REQUEST_METHOD`, `SERVER_PORT`, and `PATH_INFO`
- prints request information in the terminal
- returns the full sorted environment as a plain-text response

This file is useful for learning how request metadata reaches a WSGI app.

### 2. `reverseware.py`

This file demonstrates custom middleware through a class named `reverseware`.

Current behavior:

- wraps another WSGI application
- calls the wrapped app to get the response body
- reverses each response chunk before returning it

The wrapped application returns:

```text
Hello World
```

The middleware turns that into:

```text
dlroW olleH
```

This example is useful for understanding how middleware can intercept and transform responses.

### 3. `product-find/`

This folder contains a small path-based product lookup example.

Files:

- `product-find/main.py`: runs the WSGI app
- `product-find/inventory.py`: stores in-memory product data
- `product-find/README.md`: explains the example in detail

Current behavior:

- reads the request path from `PATH_INFO`
- uses the last path segment as a category key
- looks up product data from `inventory.py`
- returns the result as JSON text

Available example routes:

- `GET /mobile`
- `GET /laptop`

If a category is missing, the app currently returns `{}`.

### 4. `exception-handler/`

This folder demonstrates exception-handling middleware for a WSGI application.

Files:

- `exception-handler/main.py`: app, JSON helper, exception handler, and middleware
- `exception-handler/README.md`: explains the example in detail

Current behavior:

- serves product data similar to the product lookup example
- wraps the application in an `ExceptionHandler` middleware
- catches unhandled exceptions centrally
- returns a JSON `500 Internal server error` response when an exception occurs

This example is useful for learning how middleware can handle failures consistently.

## Learning Focus

Across the repository, these examples demonstrate:

- the WSGI callable pattern
- how `environ` stores request information
- how `start_response` sets status and headers
- how to return plain text and JSON responses
- how middleware can wrap applications
- how middleware can transform responses
- how middleware can centralize exception handling
- how to separate application logic from data

## Current State

This repository is still a learning sandbox, not a complete framework yet.

A few implementation details are intentionally simple:

- each example runs as a separate standalone script
- routing is path-based and minimal
- unknown product routes currently return `{}` instead of `404 Not Found`
- `product-find/main.py` currently returns JSON with `text/plain` as the content type

## Suggested Next Steps

Natural improvements for this project would be:

1. add a reusable router
2. introduce request and response helper classes
3. add proper `404 Not Found` handling
4. standardize JSON response headers across examples
5. combine middleware patterns into a more framework-like structure
