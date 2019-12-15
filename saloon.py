# TODO-1: Add Table class here
class Table:
    table_list = list()

    def __init__(self, uuid, capacity, number):
        self.uuid = uuid
        self.capacity = capacity
        self.number = number
        self.__reserved = False
        self.__is_available = True

# TODO-1: Add .sample() classmethod for Table which returns  an instance:
    @classmethod
    def sample(cls):
        return cls(uuid=5001, capacity=6, number=1)
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
