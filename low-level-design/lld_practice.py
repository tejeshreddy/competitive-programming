"""
Amazon
- Customer needs to have an account, shopping cart, checkout, browse products (search)
- Admin should be able to add products, modify products
- A customer can buy products without account
- Should be able to processs payment information
- Customer should be able to track order details
"""



import collections
import enum
from http.client import PROCESSING

class OrderDetails(enum.Enum):
    ORDERED, PACKAGED, SHIPPED, DELIVERED, LOST = 1, 2, 3, 4, 5

class AccountStatus(enum.Enum):
    ACTIVE, DEACTIVE, BLOCKED = 1, 2, 3

class PaymentStatus(enum.Enum):
    PAID, PROCESSING, REFUND = 1, 2, 3


class ZipCode:
    def __init__(self, zip_code):
        self._zip_code = zip_code

class Address:
    def __init__(self, house_number, street, city, state, zip: ZipCode):
        self._house_number = house_number
        self._street = street
        self._city = city
        self._state = state
        self._zip = zip

class Payment:
    def __init__(self, card_number, cvv, expiry, amazon_pay_id):
        pass

class CardPayment(Payment):
    def __init__(self, card_number, cvv, expiry):
        super().__init__(card_number, cvv, expiry)
    
    def card_validator() -> bool:
        pass


class AmazonPayment(Payment):
    def __init__(self, amazon_pay_id):
        super().__init__(amazon_pay_id)

class Review:
    def __init__(self, review, rating, account: Account):
        self._review = review
        self._rating = rating
        self._account = account

class Product:
    def __init__(self, product_title, sku, price):
        self._product_title = product_title
        self._sku = sku
        self._deliverable_addresses: list[ZipCode] = []
        self._reviews: list[Review] = []
        self._price = price

class ShoppingList:
    def __init__(self, list_name):
        self._shopping_list: list[Product] = []
    
    def add_product_to_shopping_list(self, product: Product) -> bool:
        self._shopping_list.append(product)

class Account:
    def __init__(self, username, password, phone, email, address: Address, account_status: AccountStatus):
        self._username = username
        self._password = password
        self._phone = phone
        self._email = email
        self._payments: list[Payment] = []
        self._addresses: list[Address] = []
        self._cart = []
        self._shopping_list = collections.defaultdict(ShoppingList)
        """
        {"clothes": ShoppingList}
        """
    
    def change_password(self, password):
        self._password = password
    
    def add_payment(self, payment: Payment) -> bool:
        self._payments.append(payment)
    
    def add_address(self, address: Address) -> bool:
        self._addresses.append(address)

    def add_to_cart(self, product: Product):
        self._cart.append(product)
    
    def add_to_shoppinglist(self, title, product):
        self._shopping_list[title].append(product)
    
    def checkout(self):
        pass




    









