from datetime import datetime


# TODO-1: Add Order model here
from finance import Bill
from saloon import Table


class Order:
    def __init__(self, uuid, item_dict, in_out, datetime, bill, table):
        self.uuid = uuid
        self.item_dict = item_dict
        self.in_out = in_out
        self.datetime = datetime
        self.bill = bill
        self.table = table

# TODO-1: Add .sample() classmethod for Order which returns an instance:
    @classmethod
    def sample(cls):
        return cls(
            uuid=2001, item_dict={'peperoni pizza': 1}, in_out='in',
            datetime=datetime.fromisoformat('2011-11-04T00:05:23'),
            bill=Bill.sample(), table=Table.sample()
        )
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
