from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import Library, Book

app = FastAPI()
my_library = Library()

class BookModel(BaseModel):
    title: str
    author: str
    isbn: int

@app.post("/add-book")
def add_book(book_data: BookModel):
    new_book = Book(
        title=book_data.title,
        author=book_data.author,
        isbn=book_data.isbn
    )
    my_library.add_book(new_book)
    return {
        "message": f"წიგნი '{new_book.title}' წარმატებით დაემატა."
    }

@app.get("/library")
def get_library():
    library_dict = my_library.read_library()
    return library_dict

@app.post("/delete-book")
def delete_book(book_title: str):
    success = my_library.remove_book(book_title)
    if not success:
        raise HTTPException(
            status_code=400,
            detail="ასეთი წიგნი ვერ მოიძებნა."
        )
    else:
        return {
        "message": f"წიგნი {book_title} წარმატებით წაიშალა."
    }

@app.get("/book/{isbn}")
def get_book(isbn: int):
    book = my_library.get_book_with_isbn(isbn)
    if not book:
        raise HTTPException(
            status_code=404,
            detail="ასეთი წიგნი ვერ მოიძებნა."
        )
    else:
        return book.get_info()
     





