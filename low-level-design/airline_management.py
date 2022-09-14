"""
Entities/Relationships
- Address
- Seat
    - SeatType
    - SeatPrice
    - User Occuping
- Flight
    - Source
    - Desitnation
    - Flight Number
    - Aircraft
    - Flight Time Start
    - Flight End Time
    - Seats
    - GetSeatInfo()
    - AddSeat()
- Airport Location
- Account
    - Username
    - Password
    - Email
    - Phone Number
    - ChangePassword()
- User
    - Account
    - CreateBooking()
    - UpdateBooking()
    - CancelBooking()
    - ViewBookings()
- Notification
    - Update On Flight
"""

from datetime import datetime
from email import message
import enum
from os import stat
from tracemalloc import start

class SeatType(enum.Enum):
    ECONOMY, BUSINESS, PREMIUM = 1, 2, 3

class SeatStatus(enum.Enum):
    BOOKED, RESERVED, HANDICAPPED, GOVERNMENT_OFFICIALS = 1, 2, 3, 4

class TicketStatus(enum.Enum):
    BOOKED, CANCELLED = 1, 2

class Address:
    def __init__(self, house_number, street, city, state, zip):
        self._house_number = house_number
        self._street = street
        self._zip = zip
        self._city = city
        self._state = state

class Payment:
    def __init__(self) -> None:
        pass

class Account:
    def __init__(self, username, email, password, phone_number, address: Address):
        self._username = username
        self._email = email
        self._password = password
        self._phone_number = phone_number
        self._address = address
        self._payment: list[Payment] = []
    
    def change_password(self, password):
        self._password = password
    
class Ticket:
    def __init__(self, flight: Flight, seat: Seat, ticket_status: TicketStatus):
        self._ticket_status = ticket_status
        pass

class User(Account):
    def __init__(self):
        self._bookings: list[Ticket] = [Ticket]
    
    def view_booking(self):
        return self._bookings

    def cancel_booking(self, ticket: Ticket):
        if ticket in self._bookings:
            self._bookings.remove(ticket)
            ticket._ticket_status = TicketStatus.CANCELLED
        else:
            raise Exception("Ticket not found under user")

class Admin(Account):
    def __int__(self):
        pass

class Seat:
    def __init__(self, user: User, seat_type: SeatType, seat_status: SeatStatus):
        self._user = user
        self._seat_type = seat_type
        self._seat_status = seat_status

class Airport:
    def __init__(self, ticker, address: Address):
        pass

class Flight:
    def __init__(self, source: Airport, destination: Airport, start_time: datetime, arrival_time: datetime):
        self._source = source
        self._destination = destination
        self._start_time = start_time
        self._seats: list[Seat] = []
        self._flight_capacity: int = 0
        self._notification_block_list: list[Seat] = []
    
    def add_seat(self, seat: Seat) -> bool:
        if len(self._seats) >= self._flight_capacity:
            raise Exception("Flight cannot be added")
        else:
            self._seats.append(seat)
    
    def remove_seat(self, seat: Seat):
        del self._seats[seat]
    
# Observer design pattern
class Notification:
    def __init__(self):
        pass

    def notifiy_change_time(self, flight: Flight):
        for seat in flight._seats:
            if seat not in flight._notification_block_list:
                self.notify(seat._user._email, "Change in flight time to {}".format(flight._start_time))
    
    def notify(self, email, message):
        pass

    def remove_subscriber(self, flight: Flight, seat: Seat):
        pass

    def add_subsriber(self, flight: Flight, seat: Seat):
        pass

