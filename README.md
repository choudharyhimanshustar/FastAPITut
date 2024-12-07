# FastAPI Overview

FastAPI is a modern, high-performance framework for building APIs with Python. It provides automatic documentation, type checking, and great support for asynchronous programming.

---

## Installation

To get started, install FastAPI and Uvicorn (a web server to run FastAPI).

  ```bash
  python -m pip install fastapi
  pip install uvicorn
  ```
# Starting a FastAPI Application

Initialize FastAPI:

---
```bash
from fastapi import FastAPI

app = FastAPI()
```
Run the Application: Use the following command to start the server:
```bash
uvicorn <file_name_without_extension>:<app_variable_name> --reload
```

## API ENDPOINTS
FastAPI supports the following HTTP methods:

GET
POST
PUT
DELETE
Example - GET Endpoint
```bash
@app.get("/")
def function_name():
    return {"message": "Hello, World!"}
```

Access it at /docs (Swagger UI).
Use this interface to test API endpoints without additional tools like Postman.

## Path Parameters
Path parameters are added to the URL for retrieving specific information.
Use {} to define dynamic path segments.
```bash
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```
Additional Validation with Path
Use the Path module to add more validations for path parameters.

## Query Parameters
Query parameters are used to pass values in the URL after ?.

```bash
@app.get("/search/")
def search(query: str = None):
    return {"query": query}
```
## Optional Query Parameters
Use Optional from typing to define optional parameters.
```bash
from typing import Optional

@app.get("/search/")
def search(query: Optional[str] = None):
    return {"query": query}
```
Best Practices:
Set a default value (None) for optional parameters.
Place optional arguments after required ones, or use * before parameters.
## Request Body and POST Method
To define the structure of the request body, use BaseModel from pydantic.

```bash
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
Create a POST Endpoint:

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
```
## PUT Method
The PUT method is used to update resources. Use optional fields in the BaseModel to allow partial updates.

```bash
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}
```
## DELETE Method
The DELETE method is used to delete resources.
```bash
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
```
