from datetime import datetime
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

app = FastAPI()


# Model for the book
class Book(BaseModel):
    id: int
    title: str
    author: str
    published_year: int

    @field_validator("published_year")
    def validate_published_year(cls, value):
        if value > datetime.now().year:
            raise ValueError("Published year cannot be in the future.")
        return value


# In-memory database
books_db = {}

# Endpoint to test the API
@app.get("/")
def read_root():
    return {"message": "Welcome to the Simple Book Management API."}

# Endpoint to create a new book
@app.post("/books", response_model=Book)
def create_book(book: Book):
    if book.id in books_db:
        raise HTTPException(status_code=400, detail="Book already exists.")
    books_db[book.id] = book
    return book


# Endpoint to get the list of all books
@app.get("/books", response_model=List[Book])
def get_books():
    return list(books_db.values())


# Endpoint to get a book by its id
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = books_db.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book


# Endpoint to update a book by its id
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found.")
    books_db[book_id] = updated_book
    return updated_book


# Endpoint to delete a book by its id
@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    book = books_db.pop(book_id, None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book
