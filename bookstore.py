from typing import Optional
from fastapi import Body, FastAPI, Path
from pydantic import BaseModel
app = FastAPI()

books = {
    1: {
        "title": "temp title",
        "author": "john",
        "description": "year 12",
        "price": 10.50,
        "stock": 15
    },

    2: {
        "title": "apple",
        "author": "Seed",
        "description": "about appleseed",
        "price": 15.60,
        "stock": 8
    },

    3: {
        "title": "house",
        "author": "Bob",
        "description": "about house",
        "price": 3.20,
        "stock": 6
    }
}

class Book(BaseModel):
    title: str
    author: str
    description: str
    price: float
    stock: int

class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None


@app.get('/')
def index():
    return {'name': 'First Data'}

# path parameter
@app.get('/books/{book_id}')
def get_book(book_id: int = Path(description="The ID of the book you wantto view", gt=0, lt=3)):
    return books[book_id]

# Query parameter
@app.get('/books')
def get_book(name: str):
    for book_id in books:
        if books[book_id]["name"] == name:
            return books[book_id]
    return {"Data": "Not Found"}

# # Query parameter (Optional)
# @app.get('/get-by-name-optional')
# def get_student(name: Optional[str] = None):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     return {"Data": "Not Found"}

# # Query parameter (Optional) - ERROR without *
# # * allows us to write parameters anywhere we want
# @app.get('/get-by-name-optional')
# def get_student(*, name: Optional[str] = None, test: int):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     return {"Data": "Not Found"}

# # combining path and query parameters
# @app.get('/get-by-name-optional/{student_id}')
# def get_student(*, student_id: int, name: Optional[str] = None, test: int):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     return {"Data": "Not Found"}

# Request Body and the Post Method
@app.post("books/{book_id}")
def create_book(book_id: int, book: Book):
    if book_id in books:
        return {"Error": "book exists"}
    books[book_id] = book
    return books[book_id]

# PUT method
@app.put("/books/{book_id}")
def update_book(book_id: int, book: UpdateBook):
    if book_id not in books:
        return {"Error": "book does not exists"}
    books[book_id] = book
    return books[book_id]

# On updating just the name, other values gets overwritten by null.
# {
# name: "alex"
# age: null
# year: null
# }

# PUT method
@app.put("/books/{book_id}")
def update_book(book_id: int, book: UpdateBook):
    if book_id not in books:
        return {"Error": "book does not exists"}
    if book.title != None:
        books[book_id].title = book.title
    if book.author != None:
        books[book_id].author = book.author
    if book.description != None:
        books[book_id].description = book.description
    if book.price != None:
        books[book_id].price = book.price
    if book.stock != None:
        books[book_id].stock = book.stock
    return books[book_id]

# On updating just the name, other values remains as it is.
# {
# name: "alex"
# age: 24
# year: 2021
# }

# Delete Method
@app.delete("/delete-book/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        return {"Error": "book does not exists"}
    del books[book_id]
    return {"Message": "book deleted successfully"}
