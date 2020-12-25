# DONE: Add Bill class here
from uuid import uuid4
from datetime import datetime
from khayyam import JalaliDatetime
from lib import Root


class Bill(Root):
    bill_list = []

    def __init__(self, total_price, payment, *args, **kwargs):
        self.total_price = total_price
        self.payment = payment
        self.uuid = uuid4()
        Bill.bill_list.append(self)
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, total_price=5):
        return cls(total_price=total_price, payment=Payment.sample())

    @classmethod
    def show_unpaid(cls):
        result = []
        for item in cls.bill_list:
            if not item.payment.is_paid:
                result.append(item)
        return result

    @classmethod
    def show_paid(cls):
        result = []
        for item in cls.bill_list:
            if item.payment.is_paid:
                result.append(item)
        return result


class Payment(Root):
    payment_list = []

    def __init__(self, price, payment_type, is_paid, *args, **kwargs):
        self.price = price
        self.payment_type = payment_type
        self.is_paid = is_paid
        self.datetime = datetime.now()
        self.uuid = uuid4()
        Payment.payment_list.append(self)
        super().__init__(*args, **kwargs)

    # DONE: Add .sample() classmethod for Bill and Payment which returns

    def pay(self):
        self.is_paid = True

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self.datetime)

    @classmethod
    def sample(cls, price=12, payment_type='cash', is_paid=False):
        return cls(price=price, payment_type=payment_type, is_paid=is_paid)

    @classmethod
    def paid_list(cls):
        result = list()
        for item in cls.payment_list:
            if item.is_paid:
                result.append(item)
        return result

    @classmethod
    def total_paid(cls):
        total = 0
        for paid in cls.payment_list:
            if paid.is_paid:
                total += paid.price
        return total

        # total = 0
        # for item in cls.paid:
        #     total += item.total_price
        # return total
# DONE: Add Payment class here


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
# DONE-2: Add jalali_datetime property to the Payment class
# DONE-3: Set valid Payment instance for payment attr in Bill instance
# DONE-3: Add show_unpaid() classmethod to the Bill class which will return a
#       list of all unpaid bills, (Implementation is up to you)
# DONE: Add show_paid() classmethod to the Bill as show_unpaid() method
# DONE: Add paid_list() classmethod to the Payment class which will just
#       return a list of payments with True `is_paid` flag.
# DONE: Add pay() method to the Payment class which set is_paid flag True
# DONE: Add total_paid() classmethod to the Payment class which return an int
#       of total paid Payments
