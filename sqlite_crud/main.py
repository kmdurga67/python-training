import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()


class BookCreate(BaseModel):
    title: str
    author: str


# class Book(BookCreate):
#     id: int


def create_connection():
    connection = sqlite3.connect("books.db")
    return connection


def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS books 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   author TEXT NOT NULL)
                   """)
    connection.commit()
    connection.close()


create_table()


def create_book(book: BookCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)",
                   (book.title, book.author))
    connection.commit()
    book_id = cursor.lastrowid  # Get the ID of the last inserted row
    connection.close()
    return book_id

# If two people are inserting at the same time, as long as they are using different cursors, cursor.lastrowid will return the id for the last row that cursor inserted
#  cursor.execute("SELECT last_insert_rowid()")
# book_id = cursor.fetchone()[0]


def get_all_books():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connection.close()
    return [{"id": book[0], "title": book[1], "author": book[2]} for book in books]


def get_book(book_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()
    connection.close()
    if book:
        return {"id": book[0], "title": book[1], "author": book[2]}


def update_book(book_id: int, book: BookCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET title=?, author=? WHERE id=?",
                   (book.title, book.author, book_id))
    connection.commit()
    connection.close()


def delete_book(book_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    # data = cursor.execute("SELECT * FROM books")
    # print(data.fetchall())
    connection.commit()
    connection.close()
    return {"message": "Book deleted successfully", "id": book_id}


@app.post("/books", response_model=dict)
def create_book_endpoint(book: BookCreate):
    book_id = create_book(book)
    return {"id": book_id, **book.dict()}


@app.get("/books", response_model=list[dict])
def read_all_books():
    books = get_all_books()
    return books


@app.get("/books/{book_id}", response_model=dict)
def read_book(book_id: int):
    book = get_book(book_id)
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}", response_model=dict)
def update_book_endpoint(book_id: int, updated_book: BookCreate):
    existing_book = get_book(book_id)
    if existing_book:
        update_book(book_id, updated_book)
        return {"message": "Book updated successfully", **updated_book.dict(), "id": book_id}
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", response_model=dict)
def delete_book_endpoint(book_id: int):
    existing_book = get_book(book_id)
    if existing_book:
        delete_book(book_id)
        return {"message": "Book deleted successfully", **existing_book}
    else:
        raise HTTPException(status_code=404, detail="Book details not found")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
