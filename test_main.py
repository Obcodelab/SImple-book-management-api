from fastapi.testclient import TestClient

from main import app, books_db

client = TestClient(app)


def test_create_book():
    response = client.post(
        "/books",
        json={
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "published_year": 1925,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
    }


def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "published_year": 1925,
        }
    ]


def test_get_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
    }


def test_update_book():
    response = client.put(
        "/books/1",
        json={
            "id": 1,
            "title": "Harry Potter",
            "author": "J.K. Rowling",
            "published_year": 1997,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "published_year": 1997,
    }


def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "published_year": 1997,
    }
    assert books_db == {}
