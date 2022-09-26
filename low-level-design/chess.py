
from ast import Add
import enum
from multiprocessing.pool import CLOSE
from pickle import PickleError
from select import KQ_FILTER_SIGNAL
from tkinter import ACTIVE

class GameStatus(enum.Enum):
    ACTIVE, BLACK_WIN, WHITE_WIN = 1, 2, 3

class AccountStatus(enum.Enum):
    ACTIVE, CLOSED, BLACKLISTED = 1, 2, 3

class Address:
    def __init__(self, house, street, city, state, zip):
        self._house = house
        self._street = street
        self._city = city
        self._state = state
        self._zip = zip

class Account:
    def __init__(self, username, password, email, phone, address, account_status: AccountStatus = AccountStatus.ACTIVE):
        self._username = username
        self._password = password
        self._email = email
        self._phone = phone
        self._address: Address = address
        self._account_status = account_status
    
    def change_password(self, password):
        self._password = password


class Person(Account):
    def __init__(self, name):
        self._name = name
        self._wins = 0
    
    def add_wins(self):
        self._wins += 1

class Box:
    def __int__(self, piece, x, y):
        self._piece = piece
        self._x = x
        self._y = y
    
    def get_peices(self):
        return self._piece
    
    def set_peice(self, piece):
        self._piece = piece
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y

from abc import ABC

class Piece(ABC):
    def __init__(self, white=False):
        self._white = white
        self._killed = False
    
    def is_white(self):
        return self._white
    
    def set_white(self, white):
        self._white = white
    
    def is_killed(self):
        return self._is_killed
    
    def set_killed(self, killed):
        self._killed = killed
    
    def can_move(self, board, start_box, end_box):
        None

class King(Piece):
    def __init__(self, white):
        self._castling = False
    
    def valid_move(self):
        pass

    def make_move(self):
        pass

class Rook(Piece):
    def __init__(self):
        pass

class Knight(Piece):
    def __init__(self, white):
        super().__init__(white)
    
    def can_move(self, board, start, end):
        if end.get_piece().is_white() != self.is_white():
            return False
        
        x = abs(start.get_x() - end.get_x())
        y = abs(start.get_y() - end.get_y())

        return x * y == 2

class Board:
    def __init__(self):
        self._boxes: list[Box] = []
    
    def reset_board(self):
        self._boxes[0][0] = Box(0, 0, Rook(True))
        self._boxes[0][1] = Box(0, 1, Knight(True))
        self._boxes[0][2] = Box(0, 1, Bishop(True))


        self._boxes[1][0] = Box(0, 1, Pawn(True))
        self._boxes[1][1] = Box(0, 1, Pawn(True))
        self._boxes[1][2] = Box(0, 1, Pawn(True))
        # ...
        self._boxes[7][0] = Box(0, 0, Rook(True))
        self._boxes[7][1] = Box(0, 1, Knight(True))
        self._boxes[7][2] = Box(0, 1, Bishop(True))

        
        



    

        


