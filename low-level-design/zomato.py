"""
Zomato Design

Entities/Relationships
1. Account
2. User
    1. Orders (1 - n)
    2. Adresses (1 - n)
    3. Payment (1 - n)
3. Address
4. Dish
    1. Name
    2. Contents
5. Cart
    1. Items (1 to n)
    2. Dish (1 to n)
6. Item
7. Order
    1. Items(1 to n)
    2. Address(1 to 1)    
    3. Payment(1 to 1)
8. Notification
9. Payment
10. Restaurant

"""
import enum
from typing import Dict

class CuisineType(enum.Enum):
    AMERICAN, INDIAN, ITALIAN = 1, 2, 3

class Ingredient(enum.Enum):
    ONIONS, GARLIC, CHICKEN = 1, 2, 3

class Address:
    def __init__(self, no, street, city, state, zip):
        self._no = no
        self._street = street
        self._city = city
        self._state = state
        self._zip = zip

class Account:
    def __init__(self, username, password, name, email, phone):
        pass

    def change_password(self, password):
        pass


class User(Account):
    def __init__(self):
        self._cart: Cart = None
        self._payments: list[Payment] = []
    
    def add_item_to_cart(self, item) -> bool:
        self._cart.append(item)
    
    def remove_from_cart(self, item):
        pass

    def process_payment(self, payment):
        pass

class Dish:
    def __init__(self, name, dish_id, cuisine_type: CuisineType):
        self._dish_id = dish_id
        self._name = name
        self._cuisine_type = cuisine_type
        self._contents: list[Ingredient] = []
    
    def add_ingredients(self, ingredient: Ingredient):
        self._contents.append(ingredient)


class Restaurant:
    def __init__(self, name, address: Address):
        self._name = name
        self._address = address
        self._price: dict[Dish, float] = {}
    
    def add_dish(self, dish: Dish, price: float):
        pass

    def update_price(self, dish, price):
        pass








