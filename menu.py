# TODO-1: Add Item class here
class Item:
    def __init__(self, uuid, name, item_type, price, time):
        self.uuid = uuid
        self.name = name
        self.item_type = item_type,
        self.price = price
        self.time = time

# TODO-1: Add .sample() classmethod for Item which returns an instance:
    @classmethod
    def sample(cls):
        return cls(uuid=1001, name='peperoni pizza', item_type='Food', price=25000, time=25)
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
