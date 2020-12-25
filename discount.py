# DONE: Add Discount class here
from lib import Root


class Discount(Root):
    discount_list = list()

    def __init__(self, code, count, start_date, end_date, percentage, minimum_order, maximum_order, *args, **kwargs):
        self.code = code
        self.count = count
        self.start_date = start_date
        self.end_date = end_date
        self.percentage = percentage
        self.minimum_order = minimum_order
        self.maximum_order = maximum_order
        Discount.discount_list.append(self)
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, code='yalda98', count=5, start_date='2020/12/2', end_date='2021/01/01', percentage=30,
               minimum_order=20000, maximum_order=300000):
        return cls(code=code, count=count, start_date=start_date, end_date=end_date, percentage=percentage,
                   minimum_order=minimum_order, maximum_order=maximum_order)
