import os
from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
from dotenv import load_dotenv

from models import Book

load_dotenv()
app = FastAPI()

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(url, key)


@app.get("/")
def root():
    return {"message": "Hello World Books API"}


@app.get("/books")
def get_books():
    books = supabase.table('books').select('*').execute()
    return books.data


@app.get("/books/{id}")
def get_books_by_id(id: int):
    books = supabase.table('books').select('*').eq("id", id).execute()
    if not books.data:
        raise HTTPException(status_code=404, detail="Book not found")
    return books.data


@app.post("/books")
def store_books(book: Book):
    new_book = supabase.table('books').insert(
        {
            "titulo": book.titulo,
            "autor": book.autor,
            "ano": book.ano
        }
    ).execute()

    return new_book.data


@app.put("/books/{id}")
def update_books(book: Book, id: int):
    updated_book = supabase.table('books').update(
        {
            "titulo": book.titulo,
            "autor": book.autor,
            "ano": book.ano
        }
    ).eq("id", id).execute()

    if not updated_book.data:
        raise HTTPException(status_code=404, detail="Book not found")

    return updated_book.data


@app.delete("/books/{id}")
def update_books(id: int):
    book = supabase.table("books").delete().eq("id", id).execute()
    if not book.data:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Book deleted successfully"}
