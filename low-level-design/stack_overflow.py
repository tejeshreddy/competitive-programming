"""
- Questions: Users can add questions
- Answers: Users can answer questions
- Comments: Comments can be added to answers of certain questions
- Tags: Questions can have tags to better help users filter them and find relavent set of questions
- Account: We can create multiple user accounts - User, Member, Admin, Moderator

"""
import enum
from gzip import BadGzipFile
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
from unicodedata import name
import datetime

class QuesitonStatus(enum.Enum):
    OPEN, CLOSED, ON_HOLD, DELETED = 1, 2, 3, 4

class AccountStatus(enum.Enum):
    ACTIVE, CLOSED, CANCELLED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5

class Address:
    def __init__(self, house_number, street, city, state, zip):
        self._house_number = house_number
        self._street = street
        self._city = city
        self._state = state
        self._zip = zip

class Account:
    def __init_(self, username, password, address: Address, email_address, phone, account_status: AccountStatus = AccountStatus.ACTIVE):
        self._username = username
        self._password = password
        self._address = address
        self._email_address = email_address
        self._reputation = 0

    def change_password(self, password):
        self._password = password
    
    def change_account_status(self, password, account_status: AccountStatus):
        if account_status == AccountStatus.CLOSED:
            return "Account is closed!"
        else:
            raise Exception("Account Status cannot be changed to this account status")

from abc import ABC

class Member(ABC):
    def __init__(self, account: Account):
        self._account = account
        self._badge = []
    
    def get_reputation(self):
        return self._account._reputation

    def create_question(self, question):
        pass

    def create_tag(self, tag):
        pass

class Moderator(Member):
    def close_quesiton(self):
        pass
    def re_open_question(self):
        pass
        
class Admin(Moderator):
    def block_member(self, account: Account):
        self._account.change_account_status = AccountStatus.BLOCKED
    
    def unblock_member(self, account: Account):
        self._account.change_account_status = AccountStatus.ACTIVE


class Tag:
    def __init__(self):
        self._name = name
        self._description = ""
        self._total_tag_mentions = 0
        self._daily_freq = 0
        self._weekly_frequency = 0

class Comment:
    def __init__(self, text, member):
        self._text = text
        self._creation_date = datetime.datetime.now()


class Answer:
    def __init__(self):
        self._comments : list[Comment] = []
        self._creation_date = datetime.datetime.now()
    
    def add_comment(self, comment: Comment):
        self._comments.add(comment)


class Question:
    def __init__(self, title, description, member_asking: Member):
        self._creation_date = datetime.datetime.now()
        self._title = title
        self._description = description
        self._member_asking = member_asking
        self._tags : list[Tag] = []
        self._answers : list[Answer] = []

    def add_tag_to_question(self, tag : Tag) -> bool:
        if tag not in self._tags:
            self._tags.append(tag)
        else:
            raise Exception("Tag already part of question")
    
    def add_answers(self, answer: Answer):
        self._answers.append(Answer)
