from entities.patron import Patron
from repositories.patron_repository import PatronRepository

class PatronService:
    def __init__(self, patron_repository: PatronRepository):
        self.patron_repository = patron_repository

    def add_patron(self, name: str):
        patron = Patron(name)
        self.patron_repository.add_patron(patron)

    def remove_patron(self, name: str):
        patron = self.patron_repository.search_patron(name)
        if patron:
            self.patron_repository.remove_patron(patron)

    def search_patron(self, name: str) -> Patron:
        return self.patron_repository.search_patron(name)