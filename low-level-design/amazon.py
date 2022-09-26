
import collections
import enum
from itertools import product
from math import prod

class OrderStatus(enum.Enum):
    UNSHIPPED, PENDING, SHIPPED, COMPLETED, CANCELLED = 1, 2, 3, 4, 5

class AcountStatus(enum.Enum):
    ACTIVE, BLOCKED, BANNED, COMPRAMISED = 1, 2, 3, 4, 5

class PaymentStatus(enum.Enum):
    UNPAID, PAID, PENDING, DECLINED = 1, 2, 3, 4

# Address -> 
class Address:
    def __init__(self, street, city, zip_code, country):
        self._street = street
        self._city = city
        self._zip_code = zip_code
        self._country = country

class Product:
    def __init__(self, product_id):
        self._product_id = product_id
        self._review = ""
        self._name = ""
        self._product_reviews: list[ProductReview] = []

class Account:
    def __init__(self, user_name, password, name, email, phone, shipping_address: Address, billing_address: Address, status=AcountStatus.ACTIVE):
        self._username = user_name
        self._password = password
        self._name = name
        self._email = email
        self._phone = phone
        self._shipping_address = shipping_address
        self._billing_address = billing_address
        self._products = []
        self._payment_methods = []
        self._product_reviews = collections.defaultdict(str)
    
    def add_product_to_cart(self, product: Product):
        self._products.append(product)
    
    def add_product_review(self, product: Product, review: str):
        if product in self._products:
            product._review = review
        else:
            raise Exception("Product is not purchased, cannot leave review!")
    
    def reset_password(self, password):
        self._password = password


from abc import ABC, abstractclassmethod

class Customer(ABC):
    def __init__(self, cart: list[Product], order):
        self._cart = cart
        self._order = order
    
    def get_shopping_cart(self):
        return self._cart
    
    def add_item_to_cart(self, product: Product):
        self._cart.append(product)

class Guest(Customer):
    def create_account(self):
        pass

class Member(Customer):
    def __init__(self, account: Account):
        self._account = account
    
    def place_order(self, order):
        pass

class ProductCategory:
    def __init__(self, name, description):
        self._name = name
        self._description = description

class ProductReview:
    def __init__(self, rating, review, reviewer):
        self._rating = rating
        self._review = review
        self._reviewer = reviewer

class ShoppingCart:
    def __init__(self):
        self._cart : list[Product] = []
    
    def add_to_shopping_cart(self, product: Product):
        self._cart.append(product)

    def remove_product_from_cart(self, product: Product) -> bool:
        if product in self._cart:
            del self._cart[product]
            return True
        else:
            return False

