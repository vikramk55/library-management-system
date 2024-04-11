from abc import ABC, abstractmethod

class TransactionRepository(ABC):
    @abstractmethod
    def add_transaction(self, transaction):
        pass