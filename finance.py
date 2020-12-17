# DONE: Add Bill class here
from uuid import uuid4
from datetime import datetime
from khayyam import JalaliDatetime


class Bill:

    def __init__(self, total_price, payment):
        self.total_price = total_price
        self.payment = payment
        self.uuid = uuid4()

    @classmethod
    def sample(cls):
        result = {
            'total_price': 23000,
            'payment': Payment.sample(),
        }
        return cls(**result)



# DONE: Add Payment class here


class Payment:

    def __init__(self, price, payment_type):
        self.price = price
        self.payment_type = payment_type
        self.is_paid = False
        self.datetime = datetime.now()
        self.uuid = uuid4()
# DONE: Add .sample() classmethod for Bill and Payment which returns

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self.datetime)

    @classmethod
    def sample(cls):
        result = {
            'price': 12000,
            'payment_type': 'cash',
        }
        return cls(**result)
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


# DONE-2: Replace all uuid attrs with uuid.uuid4() method and prevent class
#       to get from input
# DONE-2: Change datetime attr to be assigned automatically in Payment class
# DONE: Add jalali_datetime property to the Payment class
# TODO-3: Set valid Payment instance for payment attr in Bill instance
# TODO-3: Add show_unpaid() classmethod to the Bill class which will return a
#       list of all unpaid bills, (Implementation is up to you)
# TODO-3: Add show_paid() classmethod to the Bill as show_unpaid() method
# TODO-3: Add paid_list() classmethod to the Payment class which will just
#       return a list of payments with True `is_paid` flag.
# TODO-3: Add pay() method to the Payment class which set is_paid flag True
# TODO-3: Add total_paid() classmethod to the Payment class which return an int
#       of total paid Payments
