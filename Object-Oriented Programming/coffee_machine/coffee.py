"""
I declare that the following source code was written solely by me. I understand that 
copying any source code, in whole or in part, constitutes cheating, and that I will 
receive a zero on this project if I am found in violation of this policy.
"""
__class__ = "CS 1410"
__project__ = "Project 3 - Coffee Machine"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/1/2021"
__divider__ = "------------------------------------------------------------------------"

PRODUCTS = (
    {"name": "black", "recipe": ["cup", "coffee", "water"], "price": 35,},
    {"name": "white", "recipe": ["cup", "coffee", "creamer", "water",], "price": 35,},
    {"name": "sweet", "recipe": ["cup", "coffee", "sugar", "water",], "price": 35,},
    {
        "name": "white & sweet",
        "recipe": ["cup", "coffee", "sugar", "creamer", "water",],
        "price": 35,
    },
    {"name": "bouillon", "recipe": ["cup", "bouillonPowder", "water",], "price": 25,},
)


class CoffeeMachine:
    """Class for Coffee Machine"""

    def __init__(self):
        self.cash_box = CashBox()
        products = []
        for product in PRODUCTS:
            products.append(
                Product(product["name"], product["price"], product["recipe"])
            )
        self.selector = Selector(self.cash_box, products)

    def one_action(self):
        print(__divider__)
        print("    PRODUCT LIST: all 35 cents, except bouillon (25 cents)")
        print("    1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon")
        print("    Sample commands: insert 25, select 1.")
        command = input(">>> Your command:")
        command = command.strip().lower().split()
        command_opr = command[0]  # "select" in "select 1"
        command_arg = None  # "1" in "select 1"

        # Check if command is valid
        if command_opr not in ["insert", "select", "quit", "cancel"]:
            print("Invalid command.")
            return True

        # Check if command argument is an int, if it is, store it
        if len(command) > 1:
            try:
                command_arg = int(command[1])
            except ValueError:
                print("Invalid command argument.")
                return True

        # Operation insert<coin>
        if command_opr == "insert":
            if command_arg not in [5, 10, 25, 50]:
                print("INVALID AMOUNT >>>")
                print("We only take half-dollars, quarters, dimes, and nickels.")
                return True
            self.cash_box.deposit(command_arg)
            return True

        # Operation select<product>
        if command_opr == "select":
            if command_arg not in range(len(PRODUCTS)):
                print(f"{command_arg} is not a valid selection.")
                return True
            self.selector.select(command_arg)
            return True

        # Operation cancel
        if command_opr == "cancel":
            self.cash_box.return_coins()
            return True

        # Operation quit
        if command_opr == "quit":
            return False

    def total_cash(self):
        return self.cash_box.total()


class CashBox:
    """Class for Cash Box"""

    def __init__(self):
        self.credit = 0
        self.totalReceived = 0

    def deposit(self, amount):
        self.credit += amount
        print(f"Depositing {amount} cents. You have {self.credit} cents credit.")

    def return_coins(self):
        if self.credit:
            print(f"Returning {self.credit} cents.")
        self.credit = 0

    def have_you(self, amount):
        return self.credit >= amount

    def deduct(self, amount):
        self.credit -= amount
        self.totalReceived += amount
        self.return_coins()

    def total(self):
        return self.totalReceived


class Selector:
    """Class for Selector"""

    def __init__(self, cash_box, products):
        self.cash_box = cash_box
        self.products = products

    def select(self, choice_index):
        product_index = choice_index - 1
        product_price = self.products[product_index].get_price()
        if not self.cash_box.have_you(product_price):
            print("Sorry. Not enough money deposited.")
            return
        self.products[product_index].make()
        self.cash_box.deduct(product_price)


class Product:
    """Class for Product"""

    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe

    def get_price(self):
        return self.price

    def make(self):
        print(f"Making {self.name}:")
        for item in self.recipe:
            print(f"\tDispensing {item}")

    def __str__(self):
        return f"{self.name.title()}, ${self.price/100:.2f}"


def main():
    m = CoffeeMachine()
    while m.one_action():
        pass
    total = m.total_cash()
    print(f"Total cash: ${total/100:.2f}")


if __name__ == "__main__":
    main()

