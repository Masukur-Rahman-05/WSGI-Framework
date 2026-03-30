# WSGI Web Framework

This repository is a small learning project for exploring how Python WSGI applications and middleware work.

The current codebase contains two simple runnable examples:

- `main.py` shows a basic WSGI app that inspects the request environment
- `reverseware.py` shows a custom WSGI middleware that reverses the response body

## Project Structure

```text
WSGI Web Framework/
|-- main.py
|-- reverseware.py
|-- README.md
```

## Requirements

- Python 3.x

No external packages are required because the project uses Python's built-in `wsgiref.simple_server`.

## How to Run

Run either example from the project root:

```bash
python main.py
```

or:

```bash
python reverseware.py
```

Both examples start a local server on:

```text
http://localhost:8000
```

Only run one file at a time, since both use the same port.

## Example 1: `main.py`

`main.py` demonstrates the core WSGI application interface:

```python
application(environ, start_response)
```

When a request comes in, the app:

1. reads the WSGI `environ` dictionary
2. extracts request details such as method, port, and path
3. prints those values in the terminal
4. returns the full environment as a plain-text HTTP response

### Current behavior in `main.py`

- host: `localhost`
- port: `8000`
- content type: `text/plain`
- terminal log: request method, server port, and requested path
- browser response: sorted WSGI environment key/value pairs

This file is useful for learning how request metadata is passed into a WSGI app.

## Example 2: `reverseware.py`

`reverseware.py` demonstrates a custom WSGI middleware class named `reverseware`.

The middleware:

1. wraps another WSGI application
2. calls the wrapped application to get its response
3. reverses each chunk of response bytes before returning it

The wrapped app returns:

```text
Hello World
```

Because the middleware reverses the bytes, the browser receives:

```text
dlroW olleH
```

This example is useful for understanding how middleware can sit between the server and the application and transform the response.

## Learning Focus

This project currently helps demonstrate:

- the WSGI callable pattern
- how `environ` stores request information
- how `start_response` is used to send headers and status
- how to run a server with `wsgiref.simple_server`
- how middleware can wrap and modify application output

## Notes

- Stop the server with `Ctrl + C`
- Both scripts are independent examples, not a single combined framework yet
- A natural next step would be to combine these ideas into reusable routing, request, response, and middleware components
