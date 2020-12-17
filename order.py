# DONE-1: Add Order model
from uuid import uuid4
from finance import Bill
from saloon import Table
from datetime import datetime
from khayyam import JalaliDatetime
from menu import Item
from finance import Payment


class Order:
    orders_list = list()
    un_paid_orders = list()

    def __init__(self, in_out, item_dict, table=None):
        self.in_out = in_out
        self.item_dict = item_dict
        self.table = table
        self.bill = self.set_bill()
        self.uuid = uuid4()
        self.datetime = datetime.now()
# DONE-1: Add .sample() classmethod for Order which returns an instance:

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self.datetime)

# DONE-2: Add set_bill method to the Order class which create proper Bill
#       instance according to the items in the order
    def set_bill(self):
        items_price = 0
        for item in self.item_dict:
            items_price += item.price
        return Bill(total_price=items_price, payment=Payment.sample())
        # return items_price

    def assign_table(self):
        table_found = None
        for table in Table.table_list:
            if self.in_out == 'I' and table.is_available:
                self.table = table
                table.is_available = False
                table_found = True
        if not table_found:
            return 'not find any available table!'


    @classmethod
    def sample(cls):
        result = {
            'in_out': 'I',
            # 'bill': Bill.sample(),
            # 'table': Table.sample(),
            'item_dict': {Item.sample()},
        }
        return cls(**result)
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
# DONE-2: Replace all uuid attrs with uuid.uuid4() method and prevent class
# DONE-2: Add jalali_datetime property to the Order class
# DONE-2: uuid and datetime attrs should be assigned automatically
# DONE-2: Store a list of orders and a list for un_paid_orders
# DONE-2: Add assign_table method to the Order class which assign table to the
#       client and change the table status
# TODO-2: Set I/O for in_out option in Order class
