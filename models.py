class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def get_info(self):
        return {
            "title": self.__title,
            "author": self.__author,
            "isbn": self.__isbn
        }
    @property
    def title(self):
        return self.__title
    @property
    def author(self):
        return self.__author
    @property
    def isbn(self):
        return self.__isbn

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book: Book):
        self.__books.append(book)

    def read_library(self) -> list:
        return [book.get_info() for book in self.__books]

    def remove_book(self, book_title: str):
        exists = any(book.title == book_title for book in self.__books)
        if exists:
            self.__books = [book for book in self.__books if book.title != book_title]
            return True
        else:
            return False

    def get_book_with_isbn(self, isbn: int):
        return next((book for book in self.__books if book.isbn == isbn), None)

