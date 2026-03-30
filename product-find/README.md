# Product Find

This folder contains a small WSGI example that returns product data based on the request path.

It is a simple category-based product lookup service built with Python's built-in `wsgiref.simple_server`.

## Files

```text
product-find/
|-- inventory.py
|-- main.py
|-- README.md
```

## What It Does

The application reads the requested URL path, treats the last part of the path as a product category, and looks that category up inside `inventory.py`.

If the category exists, the matching product data is returned as JSON.

Current categories:

- `mobile`
- `laptop`

## How It Works

`main.py`:

- starts a WSGI server on `http://localhost:8000`
- reads `PATH_INFO` from the WSGI `environ`
- extracts the category from the URL
- looks up the category in `inventory.py`
- returns the result as JSON text

`inventory.py`:

- stores the in-memory product data used by the app

## How to Run

Open a terminal in this folder and run:

```bash
python main.py
```

Then visit one of these URLs:

```text
http://localhost:8000/mobile
http://localhost:8000/laptop
```

## Example Responses

Request:

```text
GET /mobile
```

Response:

```json
{"product_id": 1, "product_name": "samsung", "price": "$1000"}
```

Request:

```text
GET /laptop
```

Response:

```json
{"laptop_id": 1, "laptop_name": "Asus", "price": "$1500"}
```

If a category is not found, the app currently returns an empty JSON object:

```json
{}
```

## Learning Focus

This folder is useful for learning:

- how to read the request path from WSGI `environ`
- how to build a simple path-based lookup
- how to return JSON from a WSGI application
- how to separate application logic from data storage

## Notes

- The response header is currently `text/plain` even though the body contains JSON
- A good next improvement would be changing the content type to `application/json`
- Stop the server with `Ctrl + C`
