"""
This module provides the API for managing books.
"""

from typing import List
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configure CORS
origins = [
    "",  # Your frontend application URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model for a book
class Book(BaseModel):

    """Data model for a book."""

    id: int
    title: str
    author: str
    published_year: int

    def validate_published_year(self, value):
        """Validate the published_year"""
        if value > datetime.now().year:
            raise ValueError("published_year must be a valid year")
        return value

# In-memory data storage for books
books_db = {}


@app.post("/books", response_model=Book)
def create_book(book: Book):

    """Create a new book."""

    if book.id in books_db:
        raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    books_db[book.id] = book
    return book


@app.get("/books", response_model=List[Book])
def get_books():

    """Retrieve a list of all books"""

    return list(books_db.values())


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):

    """Retrieve details of a specific book by its ID"""

    book = books_db.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):

    """Update the details of a specific book by its ID"""

    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found.")
    books_db[book_id] = updated_book
    return updated_book


@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):

    """Delete a specific book by its ID"""

    book = books_db.pop(book_id, None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book
