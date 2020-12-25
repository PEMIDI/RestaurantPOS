from uuid import uuid4
from datetime import datetime
from lib import Root
# DONE: Add Item class here


class Item(Root):
    item_id = 0
    item_list = []
    food_list = list()
    beverage_list = list()
    starter_list = list()

    def __init__(self, name, item_type, price, *args, **kwargs):
        self.name = name
        self.item_type = item_type
        self.uuid = uuid4()
        self.check_item()
        self.datetime = datetime.now()
        self.price = price
        self.item_id = Item.generate_id()
        Item.item_list.append(self)
        super().__init__(*args, **kwargs)

    @classmethod
    def generate_id(cls):
        cls.item_id += 1
        return cls.item_id

    def check_item(self):
        if self.item_type == 'f':
            Item.food_list.append(self)
        elif self.item_type == 'b':
            Item.beverage_list.append(self)
        elif self.item_type == 's':
            Item.starter_list.append(self)

# DONE: Add .sample() classmethod for Item which returns an instance:
#     def sample(self):
#         result = {
#             'name': 'item1'
    @classmethod
    def sample(cls, name='pizza', item_type='f', price=1):
        return cls(name=name, item_type=item_type, price=price)

    @classmethod
    def prompt(cls):
        name = input('enter your meal name\n').lower()
        item_type = input('enter your meal type'
                          ' f for food, b for beverage, s for starter').lower()
        price = int(input('enter meal price \n'))
        result = {'name': name, 'item_type': item_type, 'price': price}
        cls(**result)

    @classmethod
    def show_menu(cls):
        for meal in Item.item_list:
            print(f"id: {meal.item_id} | {meal.name}")
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)

# DONE-2: Add item_id to the Item class, item_id should be auto incremental
# DONE-2: item_types should be assigned automatically in Item class
# DONE-2: Add jalali_datetime property to the Item class
# DONE: Add show_menu() classmethod to the be one of (f, s or b) for Food,
# Starter or Beverage
# # DONE-2: Change datetime attr to Item class which will print all
#       items in the menu
# DONE-3: Add prompt() method to the Item class which will get proper dict for
#       creating each single item from user input and return data
