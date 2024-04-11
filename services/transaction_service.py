from entities.transaction import Transaction
from entities.book import Book
from entities.patron import Patron
from repositories.transaction_repository import TransactionRepository

class TransactionService:
    def __init__(self, transaction_repository: TransactionRepository):
        self.transaction_repository = transaction_repository

    def borrow_book(self, book: Book, patron: Patron):
        transaction = Transaction(book, patron)
        self.transaction_repository.add_transaction(transaction)