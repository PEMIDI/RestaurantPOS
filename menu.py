# TODO-1: Add Item class here
class Item:
    food_list = list()
    beverage_list = list()
    starter_list = list()

    def __init__(self, uuid, name, item_type, price, datetime):
        self.uuid = uuid
        self.name = name
        self.item_type = item_type
        self.price = price
        self.datetime = datetime
        if item_type == "Food":
            Item.food_list.append(self)
        elif item_type == "Starter":
            Item.starter_list.append(self)
        else:
            Item.beverage_list.append(self)

    @classmethod
    def search(cls, uuid):
        tmp_list = list()
        tmp_list.extend(cls.food_list)
        tmp_list.extend(cls.starter_list)
        tmp_list.extend(cls.beverage_list)
        for item in tmp_list:
            if uuid == item.uuid:
                return item
        return -1

# TODO-1: Add .sample() classmethod for Item which returns an instance:
    @classmethod
    def sample(cls):
        return cls(uuid=1001, name='peperoni pizza', item_type='Food',
                   price=25000, datetime=25)
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
