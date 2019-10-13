import random


class Store:
    """
    Represents the store

    The has:
        - an inventory, that remembers how many items are in the store
        - cash, the amount of money the store has in the cash register
    """

    def __init__(self, cash: float):
        """
        Implement this method
        :param cash: the amount of cash the store has when it opens
        """

    def restock(self, item: 'Item', quantity: int):
        """
        This methods is called when the store restocks on an item

        :param item: this is the item we buy, for example "apple"
        :param quantity: this is the quantity bought by the store, for example 3
        """

    def has_enough_items(self, item: 'Item', quantity: int) -> bool:
        """
        This method is called when a client wants to buy items from the store.

        You should also check that the item exists in the store inventory

        :param item: the type of item the client wants to buy
        :param quantity: the amount of item the client wants to buy
        :return: True if the store has enough of that item, False if there isn't enough left
        """

    def sell(self, item: 'Item', quantity: int):
        """
        This method is called when the store sells a given quantity of a given Item.

        It should REMOVE the sold items from the store's inventory

        :param item: Item that has been sold
        :param quantity: amount of sold items
        """

    def __str__(self) -> str:
        """
        When we print the store, we should see a list of items currently in the store
        :return:
        """
        # REMOVE THE LINE BELOW
        return self.__repr__()


class Item:
    """
    Item represents something that the store sells

    It has:
        - a name: str, for example "banana"
        - a price; int, for example 30
    """

    def __init__(self, name: str, price: float):
        """
        Implement this method

        :param name: name of the item
        :param price: price of the item
        """

    def __str__(self) -> str:
        """
        Implement this method.

        It should return something like:
            banana (2.0€)
        """
        # REMOVE THE LINE BELOW
        return self.__repr__()

    def price_for(self, quantity: int) -> float:
        """
        This method returns the price for a given amount of this item

        :param quantity: amount of item
        :return: price as a float
        """

class Client:
    """
    Represents a client of the store.

    A client has:
        - a name: str
        - a gender: str
            - gender can be "m", for "male", or "f", for "female"
        - an age: int
        - money: float, how much money the client has at the start of the program

    When you print a client, it should show a nice string describing the person:
        Client: Joseph Oliver, male, 31y old, has 132€
        Client: Caroline Hill, female, 42y old, has 79€
        Client: James Lee, male, 32y old, has 34€
        Client: Charles Lawrence, male, 42y old, has 39€
        Client: Jonathan Slater, male, 52y old, has 51€
    """

    def __init__(self, name: str, gender: str, age: int, money: float):
        """
        Implement this method

        :param name: name of the client
        :param gender: gender of the client: "m" or "f"
        :param age: age of the client
        :param money: amount of money the client has
        """

    def __str__(self) -> str:
        """
        Implement this method

        It should return something like:
            Client: Jonathan Slater, male, 39y old, has 258€
        """
        # REMOVE THE LINE BELOW
        return self.__repr__()

    def has_enough_money_for(self, quantity: int, item: 'Item') -> bool:
        """
        This method verifies that the client has enough money for a given quantity of items

        :param quantity: integer, how many items the client wants to buy
        :param item: the Item the client wants to buy
        :return: a boolean (True or False)
            - True if the client has enough money
            - False if the client does not have enough money
        """

    def spend(self, amount: float):
        """
        This method is called when the client spend money at the store

        It removes money from the client's wallet and transfer it to the store

        :param amount: amount of money to remove
        """


def make_a_transaction(store: Store, client: Client, item: Item, quantity: int):
    """
    Implement this method

    :param store: the store that will sell the item
    :param client: the client that will buy the item
    :param item: the item itself
    :param quantity: the amount of items
    """
    print('\n')
    print('-' * 50)
    # Print the current inventory of the store

    # Print the current client

    # Print what the client wants to buy

    # What is the total price of the transaction?

    # Print a summary of the transaction: quantity of item, name of the item, total cost, cost of one item

    # Check that the store has enough of that item in stock
    # If it doesn't, abort the function (just "return")

    # Check that the client has enough money
    # If they don't, abort the function (just "return")

    # Use the "sell" method of the store to update the inventory

    # Use the "spend" method of the client to update their wallet



# DO NOT EDIT ANYTHING UNDER THIS LINE
#
CLIENTS = [
    Client(**x)
    for x in [
        {'name': 'Joseph Oliver', 'gender': 'm', 'age': random.randint(20, 60), 'money': random.randint(10, 500)},
        {'name': 'Caroline Hill', 'gender': 'f', 'age': random.randint(20, 60), 'money': random.randint(10, 500)},
        {'name': 'James Lee', 'gender': 'm', 'age': random.randint(20, 60), 'money': random.randint(10, 500)},
        {'name': 'Charles Lawrence', 'gender': 'm', 'age': random.randint(20, 60), 'money': random.randint(10, 500)},
        {'name': 'Jonathan Slater', 'gender': 'm', 'age': random.randint(20, 60), 'money': random.randint(10, 500)},
    ]
]
print('\nClients:')
for client in CLIENTS:
    print('\t', client)
ITEMS = [
    Item(**x)
    for x in [
        {'name': 'banana', 'price': 2.0},
        {'name': 'orange', 'price': 4.0},
        {'name': 'apple', 'price': 1.0},
        {'name': 'salad', 'price': 9.0},
    ]
]
print('\nItems:')
for x in ITEMS:
    print('\t', x)

STORE = Store(cash=2000.0)
for x in ITEMS:
    STORE.restock(x, random.randint(10, 100))
print('\n', 'Store:\n\t', STORE)

for _ in range(20):
    client = random.choice(CLIENTS)
    item = random.choice(ITEMS)
    quantity = random.randint(1, 10)
    make_a_transaction(store=STORE, client=client, item=item, quantity=quantity)