"""
Functional requirements:
- add, remove and edit parking floor
- add, remove and edit parking spot
- take ticket
- assign a parking spot
- scan ticket and pay price
- Pay using credit/debit card
- Also, accept cash payments
- add/modify parking rates
"""

import enum

class Vehicle(enum.Enum):
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5

class ParkingSpot(enum.Enum):
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5

class AccountStatus(enum.Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6

class ParkingTicketStatus(enum.Enum):
    ACTIVE, PAID, LOST = 1, 2, 3

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self._street = street
        self._city = city
        self._state = state
        self._zip_code = zip_code
        self._country = country

class Person:
    def __init__(self, name: str, address: Address, email: str, phone: str):
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone

class Account:
    def _init_(self, user_name: str, password: str, person: Person, status=AccountStatus.ACTIVE):
        self._user_name = user_name
        self._password = password
        self._person = person
        self._status = status
    
    def reset_password(self, password):
        self._password = password

class Admin(Account):
    def __init__(self, user_name, password, person: Person, status=AccountStatus.ACTIVE):
        super().__init__(user_name, password, person, status)
    
    def add_parking_floor(self, floor):
        pass

    def add_parking_spot(self, floor, spot):
        pass
    
    def add_customer_info_panel(self, floor_name, info_panel):
        pass

    def add_entrance_panel(self, enterance_panel):
        pass

    def add_exit_panel(self, exit_panel):
        pass

    
class ParkingAttendant(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        super().__init__(user_name, password, person, status)
    
    def process_ticket(self, ticket_number):
        pass

class ParkingSpot:
    def __init__(self, number, parking_spot_type=ParkingSpot.COMPACT):
        self._number = number
        self._parking_spot_number = parking_spot_type
        self._vehicle = None
        self._is_free = True
    
    def is_free(self):
        return self._is_free
    
    def assign_vehicle(self):
        self._vehicle = Vehicle
    
    def remove_vehicle(self):
        self._vehicle = None
        self._is_free = True

class HandicappedSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpot.HANDICAPPED)

class Vehicle:
    def __init__(self, license_number, vehicle_type:ParkingSpot, ticket=None):
        self._license_number = license_number
        self._vehicle_type = vehicle_type
        self._ticket = ticket

    def assign_ticket(self, ticket):
        self._ticket = ticket


# Commands
# address = Address("Mill Ave", "Tempe", 'AZ', "85282", "USA")
# person = Person("Tej", address, "tej@123", "12345")
# print(address._city)


