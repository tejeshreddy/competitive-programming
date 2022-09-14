"""
- Person: Player, Umpire
- Players: Entire Team, Tournment Team or Playing 11
- Game: Playing 11 and 3 Umpires
- Venue: Assosciated with a game
"""

import enum
from logging import exception
from os import stat

class MatchFormat(enum.Enum):
    T20, ODI, TEST = 1, 2, 3

class MatchResult(enum.Enum):
    LIVE, FINISHED, ABONDENED = 1, 2, 3

class Umpire(enum.Enum):
    FIELD, TV = 1, 2

class WicketType(enum.Enum):
    BOLD, CAUGHT, STUMPED, RUN_OUT, LBW, RETIRED = 1, 2, 3, 4, 5, 6

class RunType(enum.Enum):
    NORMAL, WIDE, WICKET, NO_BALL = 1, 2, 3, 4

class InningsType(enum.Enum):
    NOT_DECIDED, BAT, BALL = 1, 2, 3

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self._street = street
        self._state = state
        self._city = city
        self._zip_code = zip_code
        self._country = country

class Person:
    def __init__(self, name, address: Address, email, phone):
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone

class Contract:
    def __init__(self):
        pass

class Player:
    def __init__(self, person: Person):
        self._person = person
        self._contracts = []
    
    def add_contract(self, contract: Contract):
        self._contracts.append(contract)
    
    def remove_contract(self, contract):
        if contract in self._contracts:
            del self._contracts[contract]
            print("Contract removed")
        else:
            raise exception("Contract not found!")


class Admin:
    def __init__(self, person: Person):
        self._person = person
    
    def add_matches(self, match):
        pass

    def add_team(self, team: Team):
        None
    
    def add_tournament(self, touranment):
        None

class Umpire:
    def __init__(self, person):
        self._person = person
        self._match = None
    
    def assign_match(self, match: Match):
        self._match = match


# Team, Tournament Squad and Playing 11

class Team:
    def __init__(self, name, coach):
        self._name = []
        self._players : list[Player] = []
        self._coach : list[Player] = []
        self._tags = [] #[India A, IPL, Mumbai Indians]
        self._touranment_squad = {}
    
    def add_tournament_squad(self, tournament_squad):
        self._touranment_squad[tournament_squad.name] = tournament_squad
    
    def add_players(self, player: Player):
        self._players.append(player)
    
class TournamentSquad:
    def __init__(self):
        self._players = []
        self._tournament_stats = {}
    
    def add_player(self, player: Player):
        self._player.append(player)

class Playing11:
    def __init__(self):
        self._players : list(Player) = []
    
    def add_player(self, player: Player):
        self._players.append(player)

class Ball:
    def __init__(self, over, ball):
        self._over = over
        self._ball = ball
        self._score_at_ball = 0

class Innings:
    def __init__(self, team: Team, innings_type : InningsType = InningsType.NOT_DECIDED):
        self._team = team
        self._innings_type = innings_type
        self._balls = self.get_all_balls()
    
    def get_all_balls(self, overs):
        all_balls = []
        for over in range(overs):
            for ball in range(1, 7):
                all_balls.append(Ball(over, ball))

        return all_balls

class Match:
    def __init__(self, innings1: Innings, innings2: Innings):
        self._innings1 = innings1
        self._innings2 = innings2
        self._umpires = []
        self._stadium : Address = None
    
    def add_score(self, innings : Innings, over, ball, score):
        self.innings._balls[over * 6 + ball]._score_at_ball = score
    
    def get_score(self, innings):
        score = 0
        for ball in innings._balls:
            score += ball._score_at_ball
        return score
    
    def assign_umpire(self, umpire : Person):
        self._umpires.append(umpire)
    
    def assign_stadium(self, stadium_address: Address):
        self._stadium = stadium_address


