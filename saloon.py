# DONE: Add Table class here
from uuid import uuid4


class Table:

    table_list = list()

    def __init__(self, capacity, number):
        self.uuid = uuid4()
        self.capacity = capacity
        self.number = number
        self.reserved = False
        self.is_available = False
        Table.table_list.append(self)
# DONE: Add .sample() classmethod for Table which returns  an instance:

    @classmethod
    def sample(cls):
        result = {
            'capacity': 10,
            'number': '1'
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
