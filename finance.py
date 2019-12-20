from datetime import datetime


# TODO-1: Add Bill class here
class Bill:
    def __init__(self, uuid, total_price, payment):
        self.uuid = uuid
        self.total_price = total_price
        self.payment = payment

    @classmethod
    def sample(cls):
        return cls(
            uuid=3001, total_price=107000, payment=Payment.sample()
        )


# TODO-1: Add Payment class here
class Payment:
    def __init__(self, uuid, payment_type, datetime, price):
        self.uuid = uuid
        self.payment_type = payment_type
        self.is_paid = False
        self.datetime = datetime
        self.price = price

    @classmethod
    def sample(cls):
        return cls(
            uuid=4001, payment_type='Cash',
            datetime=datetime.fromisoformat('2011-11-04T00:05:23'),
            price=107000)

# TODO-1: Add .sample() classmethod for Bill and Payment which returns
# an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
