from abc import ABC, abstractmethod

class PatronRepository(ABC):
    @abstractmethod
    def add_patron(self, patron):
        pass
    
    @abstractmethod
    def remove_patron(self, patron):
        pass
    
    @abstractmethod
    def search_patron(self, name):
        pass