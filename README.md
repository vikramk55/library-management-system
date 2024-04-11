```markdown
# Library Management System

This project is a simple library management system implemented in Python, adhering to SOLID principles. It provides functionalities to manage books, patrons, and transactions.

## File Structure

```
library_management_system/
│
├── entities/
│   ├── book.py
│   ├── patron.py
│   └── transaction.py
│
├── repositories/
│   ├── book_repository.py
│   ├── patron_repository.py
│   ├── transaction_repository.py
│   └── in_memory_repository.py
│
├── services/
│   ├── book_service.py
│   ├── patron_service.py
│   └── transaction_service.py
│
└── tests/
    ├── test_book_service.py
    ├── test_patron_service.py
    └── test_transaction_service.py
```

## Usage

1. **Clone the Repository**:
   ```
   git clone https://github.com/vikramk55/library-management-system.git
   ```

2. **Set Up Environment**:
   ```
   cd library_management_system
   python -m venv venv
   source venv/bin/activate (for Linux/Mac) or venv\Scripts\activate (for Windows)
   ```

3. **Python Prerequisite**:
   - This project requires Python version 3.7 or higher.

4. **Run Tests**:
   ```
   python -m unittest discover -s tests -p test_*.py
   ```

## Testing

The project includes unit tests for each service class:
- `test_book_service.py` for `BookService`
- `test_patron_service.py` for `PatronService`
- `test_transaction_service.py` for `TransactionService`

To run tests, execute the following command from the project root directory:
```
python -m unittest discover -s tests -p test_*.py
```

## File Explanation

- **entities/book.py**: Defines the `Book` class representing a book entity with attributes `title` and `author`.
  
- **entities/patron.py**: Defines the `Patron` class representing a library patron with attribute `name`.
  
- **entities/transaction.py**: Defines the `Transaction` class representing a borrowing transaction with attributes `book`, `patron`, and `date_borrowed`.
  
- **repositories/book_repository.py**: Defines the abstract class `BookRepository` with methods for managing books (`add_book`, `remove_book`, `search_book`).
  
- **repositories/patron_repository.py**: Defines the abstract class `PatronRepository` with methods for managing patrons (`add_patron`, `remove_patron`, `search_patron`).
  
- **repositories/transaction_repository.py**: Defines the abstract class `TransactionRepository` with a method for managing transactions (`add_transaction`).
  
- **repositories/in_memory_repository.py**: Contains concrete implementations of repositories (`InMemoryBookRepository`, `InMemoryPatronRepository`, `InMemoryTransactionRepository`).

- **services/book_service.py**: Defines the `BookService` class responsible for book-related business logic (e.g., adding, removing, searching books).
  
- **services/patron_service.py**: Defines the `PatronService` class responsible for patron-related business logic (e.g., adding, removing, searching patrons).
  
- **services/transaction_service.py**: Defines the `TransactionService` class responsible for transaction-related business logic (e.g., borrowing books).
  
- **tests/test_book_service.py**: Contains unit tests for the `BookService` class.
  
- **tests/test_patron_service.py**: Contains unit tests for the `PatronService` class.
  
- **tests/test_transaction_service.py**: Contains unit tests for the `TransactionService` class.

## Alignment with SOLID Principles

1. **Single Responsibility Principle (SRP)**:
   - Each class has a single responsibility: managing book data, patron data, or transaction data.

2. **Open/Closed Principle (OCP)**:
   - The system is open for extension (e.g., adding new services) but closed for modification (existing classes are not modified to accommodate changes).

3. **Liskov Substitution Principle (LSP)**:
   - Subclasses can be substituted for their base class without affecting behavior (e.g., `InMemoryBookRepository` can be substituted for `BookRepository`).

4. **Interface Segregation Principle (ISP)**:
   - Clients (services) are not forced to depend on interfaces they don't use (e.g., `BookService` only depends on `BookRepository`).

5. **Dependency Inversion Principle (DIP)**:
   - High-level modules (services) depend on abstractions (repositories) rather than concrete implementations (e.g., `BookService` depends on `BookRepository`).

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```