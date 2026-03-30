# WSGI Web Framework

This repository is a small learning project for understanding how a Python WSGI application works.

At the moment, the codebase contains a minimal WSGI app that:

- starts a local HTTP server with Python's built-in `wsgiref.simple_server`
- listens on `http://localhost:8000`
- returns the current WSGI `environ` contents as plain text

## Project Structure

```text
WSGI Web Framework/
|-- main.py
|-- README.md
```

## Requirements

- Python 3.x

No external packages are required.

## How to Run

From the project root, run:

```bash
python main.py
```

You should see:

```text
Server is listening to http://localhost:8000
```

Then open the following URL in your browser:

```text
http://localhost:8000
```

## What the App Does

The `application` function in `main.py` follows the WSGI callable pattern:

```python
application(environ, start_response)
```

When a request reaches the server:

1. the app reads the WSGI environment dictionary
2. it formats the environment values into plain text
3. it sends a `200 OK` response
4. it returns the response body as UTF-8 encoded bytes

This makes the project a useful starting point for learning:

- how WSGI apps receive request data
- how a response is constructed
- how Python can serve HTTP requests without a third-party framework

## Current Behavior

- Host: `localhost`
- Port: `8000`
- Content type: `text/plain`
- Response body: sorted WSGI environment key/value pairs

## Learning Goal

This project is a foundation for building a simple web framework step by step. A natural next step would be to add:

- routing
- request/response helper classes
- middleware support
- template rendering
- basic error handling

## Notes

The current server runs forever using:

```python
server.serve_forever()
```

Stop it with `Ctrl + C` in the terminal.
