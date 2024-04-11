from datetime import datetime

class Transaction:
    def __init__(self, book, patron):
        self.book = book
        self.patron = patron
        self.date_borrowed = datetime.now()
