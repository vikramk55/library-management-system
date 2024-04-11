from abc import ABC, abstractmethod

class BookRepository(ABC):
    @abstractmethod
    def add_book(self, book):
        pass
    
    @abstractmethod
    def remove_book(self, book):
        pass
    
    @abstractmethod
    def search_book(self, title):
        pass