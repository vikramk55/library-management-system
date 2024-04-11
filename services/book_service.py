from entities.book import Book
from repositories.book_repository import BookRepository

class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def add_book(self, title: str, author: str):
        book = Book(title, author)
        self.book_repository.add_book(book)

    def remove_book(self, title: str):
        book = self.book_repository.search_book(title)
        if book:
            self.book_repository.remove_book(book)

    def search_book(self, title: str) -> Book:
        return self.book_repository.search_book(title)