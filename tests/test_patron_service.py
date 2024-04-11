import unittest
from services.patron_service import PatronService
from repositories.in_memory_repository import InMemoryPatronRepository

class TestPatronService(unittest.TestCase):
    def setUp(self):
        self.patron_repository = InMemoryPatronRepository()
        self.patron_service = PatronService(self.patron_repository)

    def test_add_patron(self):
        self.patron_service.add_patron("Alice")
        patron = self.patron_service.search_patron("Alice")
        self.assertIsNotNone(patron)
        self.assertEqual(patron.name, "Alice")

    def test_remove_patron(self):
        self.patron_service.add_patron("Alice")
        self.patron_service.remove_patron("Alice")
        patron = self.patron_service.search_patron("Alice")
        self.assertIsNone(patron)

if __name__ == "__main__":
    unittest.main()