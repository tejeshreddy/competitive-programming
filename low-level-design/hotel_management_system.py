"""
Requirements:

- The applicaiton should support booking rooms of different types - 1B, 2B, Presidential Suite
- Guest shoud be able to look for a room before booking
- Booking information should be retrieved
- Application should send a notification if the booking is in 24 hours
- The system should keep track of all housekeeping tasks
- Any customer should be able to add room service and food
- Customer should be able to pay their bills using credit, debit or any form of online payment system

"""

import enum
from tkinter.ttk import Style

class RoomStyle(enum.Enum):
    STANDARD, DELUX, FAMILY_STYLE, BUSINESS_SUITE = 1, 2, 3, 4

class RoomStatus(enum.Enum):
    AVAILABLE, RESERVED, OCCUPIED, NOT_AVAILABLE, BEING_SERVICED, OTHER = 1, 2, 3, 4, 5, 6

class BookingStatus(enum.Enum):
    REQUESTED, PENDING, CONFIRMED, CHECKED_IN, CHECKED_OUT, CANCELLED, ABANDONED = 1, 2, 3, 4, 5, 6, 7

class AccountStatus(enum.Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5

class AccountType(enum.Enum):
    MEMBER, GUEST, MANAGER, RECEPTIONIST = 1, 2, 3, 4

class Account:
    def __init__(self, id, password, status=AccountStatus.ACTIVE):
        self._id = id
        self._password = password
        self._status = status

    def reset_password():
        pass

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone
        self._account = account
    
class Guest(Person):
    def __init__(self):
        self._total_checked_rooms = 0
    
    def get_bookings(self):
        pass
    
    def change_booking(self):
        pass

class Receptionist(Person):
    def search_memeber(self, name="", phone_number=None):
        pass

    def create_booking(self):
        pass

class Server(Person):
    def add_room_charge(self, room, room_charge):
        pass

class HotelLocation:
    def __init__(self, name, address):
        self._name = name
        self._address = address
    
    def get_rooms(self):
        pass

class Hotel:
    def __init__(self, name):
        self._name = name
        self._locations = [] # Array of HotelLocation


class Search:
    def search(self, style, start_date, duration):
        pass


class Room:
    def __init__(self, room_number, room_style, status, price, is_smoking):
        self._room_number = room_number
        self._room_style = room_style
        self._status = status
        self._price = price
        self._is_smoking = is_smoking
        self._keys = []
        self._house_keeping_log = []
    
    def is_room_available(self):
        pass

    def check_in(self):
        pass

    def check_out(self):
        pass

    def search(self, style, start_date, duration):
        # return all rooms with a given style, start_date and duration
        pass

class RoomKey:
    def __init__(self, key_id, barcode, is_active, is_master):
        self._key_id = key_id
        self._barcode = barcode
        self._is_active = is_active
        self._is_master = is_master

    def assign_room(self, room):
      pass

    def is_active(self):
        pass

import datetime

class RoomHouseKeeping:
    def __init__(self, description, duration, house_keeper):
        self._description = description
        self._start_date_time = datetime.date.today()
        self._duration = duration
        self._house_keeper = house_keeper











