import unittest
from services.book_service import BookService
from repositories.in_memory_repository import InMemoryBookRepository

class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_repository = InMemoryBookRepository()
        self.book_service = BookService(self.book_repository)

    def test_add_book(self):
        self.book_service.add_book("Clean Code", "Robert C. Martin")
        book = self.book_service.search_book("Clean Code")
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Clean Code")

    def test_remove_book(self):
        self.book_service.add_book("Clean Code", "Robert C. Martin")
        self.book_service.remove_book("Clean Code")
        book = self.book_service.search_book("Clean Code")
        self.assertIsNone(book)

if __name__ == "__main__":
    unittest.main()