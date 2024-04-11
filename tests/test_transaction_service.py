import unittest
from entities.book import Book
from entities.patron import Patron
from repositories.in_memory_repository import InMemoryTransactionRepository
from services.transaction_service import TransactionService

class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self.transaction_repository = InMemoryTransactionRepository()
        self.transaction_service = TransactionService(self.transaction_repository)

    def test_borrow_book(self):
        book = Book("Clean Code", "Robert C. Martin")
        patron = Patron("Alice")
        self.transaction_service.borrow_book(book, patron)
        transactions = self.transaction_repository.get_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].book.title, "Clean Code")
        self.assertEqual(transactions[0].patron.name, "Alice")

if __name__ == "__main__":
    unittest.main()