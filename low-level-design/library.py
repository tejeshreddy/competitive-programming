"""
- Different type of Books - Paperback, Hardback, Electronic, Magazine
- Bookstatus - available, reserved, lost
- Users can rent books, return books, lend books, browse books
- Admin can add books to library, remove books from library
- Person can have an account
- System should be able to fine if the users have taken the book beyond a fixed set of days
"""

from datetime import datetime
import enum

class BookType(enum.Enum):
    PAPERBACK, HARDBOUND, ELECTRONIC, MAGAZINE, JOURNAL = 1, 2, 3, 4, 5

class BookStatus(enum.Enum):
    AVAILABLE, RESERVED, LOST = 1, 2, 3

class AccountStatus(enum.Enum):
    ACTIVE, CLOSED, CANCELLED = 1, 2, 3

class BookFee(enum.Enum):
    LATE_FEE, LOST_FEE = 10, 500

class Address:
    def __init__(self, house_number, street, city, state, country):
        self._house_number = house_number
        self._street = street
        self._city = city
        self._state = state
        self._country = country

class Account:
    def __init__(self, username, password, email, phone, address: Address, account_status: AccountStatus = AccountStatus.ACTIVE):
        self._username = username
        self._password = password
        self._email = email
        self._phone = phone
        self._address = address
        self._account_status = account_status
        self._books_borrowed: list[Book] = []
        self._books_lent: list[Book] = []
    
    def change_password(self, password):
        self._password = password

class Book:
    def __init__(self, title, isbn, edition, author):
        self._title = title
        self._isbn = isbn
        self._edtion = edition
        self._author = author
        self._date_of_rental = datetime
        self._rental_per_day: float = 12.5
        self._book_rental_allowance = 10

class Rack:
    def __init__(self):
        self._rack: list[Book] = []

    def add_book_to_rack(self, book: Book) -> bool:
        self._rack.append(book)
    
    def remove_book_from_rack(self, book: Book) -> bool:
        if book in self._rack:
            del self._rack[book]
        else:
            raise Exception("Book not present in rack!")

class Library:
    def __init__(self, address: Address):
        self._racks: list[Rack] = []
    
    def add_rack(self, rack: Rack) -> bool:
        pass

    def add_book_to_rack(self, book: Book, rack: Rack) -> bool:
        pass
    
    def checkout_book(self, book: Book, account: Account) -> bool:
        account._books_lent.append(book)
    
    def get_bill(self, book: Book, account: Account) -> float:
        amount = 0.0
        days = datetime.date - book._date_of_rental
        if days <= book._book_rental_allowance:
            amount += days * book._rental_per_day
        else:
            amount += days * book._book_rental_allowance + (days - book._book_rental_allowance) * BookFee.LATE_FEE
        return amount


class Librarian(Account):
    def __init__(self, username, password, account_status: AccountStatus = AccountStatus.ACTIVE):
        super().__init__(username, password, account_status)
    
    def add_book_item(self, book: Book):
        pass

    def block_member(self, account: Account) -> bool:
        pass

    def un_block_members(self, account: Account) -> bool:
        pass


