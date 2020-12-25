# DONE: Add Table class here
from uuid import uuid4
from lib import Root


class Table(Root):
    table_list = list()

    def __init__(self, capacity, number, *args, **kwargs):
        self.uuid = uuid4()
        self.capacity = capacity
        self.number = number
        self.reserved = False
        self.is_available = False
        Table.table_list.append(self)
        super().__init__(*args, **kwargs)
# DONE: Add .sample() classmethod for Table which returns  an instance:

    @classmethod
    def sample(cls, capacity=10, number=1):
        return cls(capacity=capacity, number=number)

# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
