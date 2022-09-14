"""
Requirements

- A user should be able to rent any class of vehicle - motorcycle, 4 wheeler, quad, vans and suvs (extnedable)
- Each user can rent a max of 1 vehicle a time
- Penalize if a user has taken the vehicle for more than the fixed amt of time
"""

from datetime import date, datetime
import enum
from itertools import count
from os import stat

class Address:
    def __init__(self, house_no, street, city, state, country):
        self._house_no = house_no
        self._street = street
        self._city = city
        self._state = state
        self._country = country

class VehicleType(enum.Enum):
    FOUR_WHEELER, MOTORCYCLE, QUAD, BOAT, CHARTED_FLIGHT = 1, 2, 3, 4, 5

class VehicleStatus(enum.Enum):
    RESERVED, CURRENTLY_IN_USE, BLOCKED, DAMAGED, UNDER_SERVICE = 1, 2, 3, 4, 5

class AccountClass(enum.Enum):
    REGULAR, SILVER, GOLD, PLATINUM = 1, 2, 3, 4

class AccountType(enum.Enum):
    SAFE, UNSAFE, BLOCKED = 1, 2, 3

class RentalFee(enum.Enum):
    REGULAR, SILVER, GOLD, PLATINUM, HOURLY_FINE = 100, 80, 60, 40, 150

class Insurance:
    def __init__(self, name):
        pass

    def add_insurance(self):
        pass


class Account:
    def __init__(self, name, username, password, email, phone, insurance : Insurance, account_type: AccountType, account_class: AccountClass):
        pass

    def change_password(self, password):
        self._password = password

class Vehicle:
    def __init__(self, registeration_number, vehcile_type : VehicleType, vehicle_status : VehicleStatus):
        self._registeration_number = registeration_number
        self._vehicle_type = vehcile_type
        self._vehicle_status = vehicle_status

class RentalAgency:
    def __init__(self, address: Address):
        self._cars : list[Vehicle] = []
    
    def add_cars(self, car: Vehicle):
        self._cars.append(car)


class Reservation:
    def __init__(self, vehicle : Vehicle, start_date : datetime, end_date : datetime, actual_reserved_hours: int):
        self._vehicle = vehicle
        self._start_date = start_date
        self._end_date = end_date
        self._actual_reserved_hours = actual_reserved_hours
        self._fee = 0
    
    def calculate_rental_fee(self, fee_payment : RentalFee):
        hours = (self._end_date - self._start_date + 1)
        
        # Fixed Pay
        self._fee = self._actual_reserved_hours * fee_payment
        if hours >= self._actual_reserved_hours:
            self._fee += (hours - self._actual_reserved_hours) * fee_payment.HOURLY_FINE
        return self._fee

class Member:
    def __init__(self, account: Account):
        self._reservation : Reservation = None
        self._account = account
        pass

    def check_car_availability(self, address: Address, vehicle_type: VehicleType):
        pass

    def book_car(self, address: Address, vehicle_type: VehicleType, car: Vehicle, start_date: datetime, end_date: datetime):
        pass

    def cancel_reservation(self, reservation : Reservation):
        pass

    def get_price_of_reservation(self):
        return self._reservation.calculate_rental_fee()

