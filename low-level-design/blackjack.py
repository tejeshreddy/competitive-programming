from datetime import datetime
import enum
from logging import handlers
import numbers

class SUIT(enum.Enum):
    HEART, SPADE, CLUB, DIAMOND = 1, 2, 3, 4

class Card:
    def __init__(self, suit, face_value):
        self._suit = suit
        self._face_value = face_value
    
    def get_suit(self):
        return self._suit
    
    def get_face_value(self):
        return self._face_value

class BlackJackCard(Card):
    def __init__(self, suit, face_value):
        super().__init__(suit, face_value)

        self._game_value = face_value
        if self._game_value > 10:
            self._game_value = 10
    
    def get_game_value(self):
        return self._game_value

class Deck:
    def __init__(self):
        self._cards = []
        self._creation_date = datetime.date.today()

        for value in range(1, 14):
            for suit in SUIT:
                self._cards.append(BlackJackCard(suit, value))
    
    def get_cards(self):
        self._cards

class Shoe:
    def __init__(self, number_of_decks):
        self._cards = []
        self._number_of_decks = number_of_decks
        self.create_shoe()
        self.shuffle()
    
    def create_shoe(self):
        for deck in range(0, self._number_of_decks):
            self._cards.append(Deck().get_cards())

    def shuffle():
        pass

    def deal_card(self):
        if len(self._cards) > 0:
            return self._cards.pop(0)
        else:
            self.create_shoe()

class Hand:
    def __init__(self, black_jack_card_1, black_jack_card_2):
        self._cards = [black_jack_card_1, black_jack_card_2]
        self.max_total = 0

    def get_scores(self):
        self.totals = []
        
    def resolve_totals(self):

        for total in self.totals:
            if total > self.max_total and total <= 21:
                self.max_total = total        
        return self.max_total    

from abc import ABC, abstractmethod

class BasePlayer(ABC):
    def __init__(self, id, password, balance, status, person):
        self._id = id
        self._password = password
        self._balance = balance
        self._status = status
        self._person = person
        self._hands = []

    def reset_passwords(self, password):
        self._password = password

    def add_hand(self, hand):
        self._hand = hand

    def get_hands(self):
        return self._hands
    
    def remove_hand(self):
        self._hands = []

class Player(BasePlayer):
    def __init__(self, id, password, balance, status, person):
        super().__init__(id, password, balance, status, person)
        self._bet = 0
        self._total_cash = 0

class Dealer(BasePlayer):
    def __init__(self, id, password, balance, status, person):
        super().__init__(id, password, balance, status, person)

class Game:
    def __init__(self, player: Player, dealer: Dealer):
        self._player = player
        self._dealer = dealer
        self._MAX_DECKS = 3
        self._shoe = Shoe(self._MAX_DECKS)
    
    def start(self):
        self._player.place_bet(get_bet_from_UI())
        player_hand = Hand(self._shoe.deal_card(), self._shoe.deal_card())
        self._player._hand = player_hand

        dealer_hand = Hand(self._shoe.deal_card(), self._shoe.deal_card())
        self._dealer._hand = dealer_hand

        


def main():
    player = Player()        
    dealer = Dealer()
    game = Game(player, dealer)
    game.start()






