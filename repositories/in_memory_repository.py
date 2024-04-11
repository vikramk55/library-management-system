from repositories.book_repository import BookRepository
from repositories.patron_repository import PatronRepository
from repositories.transaction_repository import TransactionRepository

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books = [b for b in self.books if b.title != book.title]

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

class InMemoryPatronRepository(PatronRepository):
    def __init__(self):
        self.patrons = []

    def add_patron(self, patron):
        self.patrons.append(patron)

    def remove_patron(self, patron):
        self.patrons = [p for p in self.patrons if p.name != patron.name]

    def search_patron(self, name):
        for patron in self.patrons:
            if patron.name == name:
                return patron
        return None

class InMemoryTransactionRepository(TransactionRepository):
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions
