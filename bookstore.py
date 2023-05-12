from typing import Optional
from fastapi import Body, FastAPI, Path
from pydantic import BaseModel
app = FastAPI()

books = {
    1: {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "description": "The Catcher in the Rye is an American novel by J. D. Salinger that was partially published in serial form 1945–46 before being novelized in 1951. Originally intended for adults, it is often read by adolescents for its themes of angst and alienation, and as a critique of superficiality in society.",
        "price": 8.93,
        "stock": 7
    },

    2: {
        "title": "Animal Farm",
        "author": "George Orwell",
        "description": "Animal Farm is a beast fable, in the form of a satirical allegorical novella, by George Orwell, first published in England on 17 August 1945. It tells the story of a group of farm animals who rebel against their human farmer, hoping to create a society where the animals can be equal, free, and happy.",
        "price": 10.76,
        "stock": 1
    },

    3: {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "description": "To Kill a Mockingbird is a novel by the American author Harper Lee. It was published in 1960 and was instantly successful. In the United States, it is widely read in high schools and middle schools",
        "price": 8.89,
        "stock": 2
    },

    4: {
        "title": "The Story",
        "author": "A'Ziah King",
        "description": "about house",
        "price": 28.00,
        "stock": 40
    },

    5: {
        "title": "Gump and Co.",
        "author": "Winston Groom",
        "description": "Gump & Co. is a 1995 novel by Winston Groom. It is the sequel to his 1986 novel Forrest Gump and the Academy Award-winning 1994 film of the same name starring Tom Hanks. It was written to chronicle Forrest's life throughout the 1980s.",
        "price": 16.89,
        "stock": 15
    },

    6: {
        "title": "The Metamorphosis",
        "author": "Franz Kafka",
        "description": "Metamorphosis is a novella written by Franz Kafka which was first published in 1915. One of Kafka's best-known works, Metamorphosis tells the story of salesman Gregor Samsa, who wakes one morning to find himself inexplicably transformed into a huge insect and subsequently struggles to adjust to this new condition.",
        "price": 10.79,
        "stock": 2
    },

    7: {
        "title": "White Nights",
        "author": "Fyodor Dostoevsky",
        "description": "When his plane makes an emergency landing in Siberia, ballet dancer Nikolai Rodchenko (Mikhail Baryshnikov) is recognized as a defector and brought into custody. Returned to Leningrad and reunited with his former love, aging prima ballerina Galina Ivanova (Helen Mirren), Nikolai meets American dancer Raymond Greenwood (Gregory Hines), who defected to the Soviet Union during the Vietnam War but has secretly grown disenchanted. Together, they plot an escape to the American consulate and freedom.",
        "price": 7.19,
        "stock": 6
    },

    8: {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "description": "Fahrenheit 451 is a 1953 dystopian novel by American writer Ray Bradbury. Fahrenheit 451 presents an American society where books have been personified and outlawed and 'firemen' burn any that are found.",
        "price": 8.89,
        "stock": 9
    },

    9: {
        "title": "A Clockwork Orange",
        "author": "Anthony Burgess",
        "description": "A Clockwork Orange is a dystopian satirical black comedy novel by English writer Anthony Burgess, published in 1962. It is set in a near-future society that has a youth subculture of extreme violence.",
        "price": 17.89,
        "stock": 21
    },

    10: {
        "title": "A Moveable Feast",
        "author": "Ernest Hemingway",
        "description": "A Moveable Feast is a 1964 memoir and belles-lettres by American author Ernest Hemingway about his years as a struggling expat journalist and writer in Paris during the 1920s. It was published posthumously.",
        "price": 10.99,
        "stock": 12
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

# Query parameter (Optional)
@app.get('/get-by-name-optional')
def get_book(name: Optional[str] = None):
    for book_id in books:
        if books[book_id]["name"] == name:
            return books[book_id]
    return {"Data": "Not Found"}

# Query parameter (Optional) - ERROR without *
# * allows us to write parameters anywhere we want
@app.get('/get-by-name-optional')
def get_student(*, name: Optional[str] = None, test: int):
    for book_id in books:
        if books[book_id]["name"] == name:
            return books[book_id]
    return {"Data": "Not Found"}

# combining path and query parameters
@app.get('/get-by-name-optional/{student_id}')
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for book_id in books:
        if books[book_id]["name"] == name:
            return books[book_id]
    return {"Data": "Not Found"}

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
