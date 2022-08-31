"""
- The customer has to be able to book movie tickets
- Be able to purchase additional things like food and parking tickets
- Should he able to pay using multiple methods - debit card, credit cards or online platforms (amazon pay, venmo etc)
- The admin should be able to add theaters, seats
- class: Address (it can help with customer address or theater address)
- class: Theater, Seat
"""

import email
import enum


class Address:
    def __init__(self, street, city, country, zip_code):
        self._street = street
        self._city = city
        self._country = country
        self.zip_code = zip_code

class BookingStatus(enum.Enum):
    CONFIRMED, BLOCKED, INPROGRESS, CANCELLED = 1, 2, 3, 4

class SeatType(enum.Enum):
    REGULAR, PREMIUM, ACCESSIBLE, EMERGENCY_EXIT = 1, 2, 3, 4

class AccountStatus(enum.Enum):
    ACTIVE, BLOCKED = 1, 2

class Account:
    def __init__(self, username, password, email, phone_number, account_status: AccountStatus = AccountStatus.ACTIVE):
        self._username = username
        self._password = password
        self._email = email
        self._phone_number = phone_number
        self._account_status = account_status
    
    def change_password(self, password):
        self._password = password
    
from abc import ABC

class Person(ABC):
    def __init__(self, name, phone, email, account: Account):
        self._name = name
        self._account = account
        self._email = email
        self._phone = phone
    
class Customer(Person):
    def make_booking(self):
        pass

    def get_booking(self):
        pass

class Admin(Person):
    def add_movie(self):
        pass

    def add_show(self):
        pass

    def block_user(self):
        pass

class Guest:
    def make_booking(self):
        pass

    def register_account(self):
        pass

class Theater:
    def __init__(self, address: Address):
        self._address = address
        self._seats : list[Seat] = []
    
    def create_seats(self, count, type: SeatType, price):
        for seat_number in range(count):
            self._seats.append(Seat(seat_number, type, price))

class Show:
    def __init__(self, id, played_at: Theater, movie: Movie, start_time, end_time):
        self._id = id
        self._played_at = played_at
        self._movie = Movie
        self._start_time = start_time
        self._end_time = end_time

class Movie:
    def __init__(self, title, description, duration, language: list[str], release_date, genre, added_by):
        self._title = title
        self._description = description
        self._duration = duration
        self._language = language
        self._release_date = release_date
        self._genre = genre
        self._added_by = added_by
    
        self._shows = []
    
    def add_shows(self):
        pass

    def get_shows(self):
        pass

class Seat:
    def __init__(self, seat_id: str, seat_type: SeatType, price: int):
        self._seat_id = seat_id
        self._seat_type = seat_type
        self._price = price

class Payment(ABC):
    def __init__(self):
        pass

class Card(Payment):
    def __init__(self):
        pass

class WalletPayment(Payment):
    def __init__(self):
        pass

class Booking:
    def __init__(self, booking_number, number_of_seats, seats: list[Seat], booking_status: BookingStatus, payment_method: Payment):
        self._booking_number = booking_number
        self._number_of_seats = number_of_seats
        self._seats = seats
        self._booking_status = booking_status
        self.payment = payment_method



    

    



