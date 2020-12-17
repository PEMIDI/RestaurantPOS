# DONE-1: Add Order model
from uuid import uuid4
from finance import Bill
from saloon import Table
from datetime import datetime


class Order:

    def __init__(self, in_out, bill, table, item_dict):
        self.in_out = in_out
        self.bill = bill
        self.table = table
        self.item_dict = item_dict
        self.uuid = uuid4()
        self.datetime = datetime.now()
# DONE-1: Add .sample() classmethod for Order which returns an instance:

    @classmethod
    def sample(cls):
        result = {
            'in_out': 'out',
            'bill': Bill.sample(),
            'table': Table.sample(),
            'item_dict': {'pizza', 'kabab'}
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
# TODO-2: Replace all uuid attrs with uuid.uuid4() method and prevent class
# TODO-2: Add jalali_datetime property to the Order class
# TODO-2: uuid and datetime attrs should be assigned automatically
# TODO-2: Store a list of orders and a list for un_paid_orders
# TODO-2: Add set_bill method to the Order class which create proper Bill
#       instance according to the items in the order
# TODO-2: Add assign_table method to the Order class which assign table to the
#       client and change the table status
# TODO-2: Set I/O for in_out option in Order class
