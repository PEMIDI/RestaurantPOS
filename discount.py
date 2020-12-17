# DONE: Add Discount class here

class Discount:

    def __init__(self, code, count, start_date, end_date, percentage, minimum_order, maximum_order):
        self.code = code
        self.count = count
        self.start_date = start_date
        self.end_date = end_date
        self.percentage = percentage
        self.minimum_order = minimum_order
        self.maximum_order = maximum_order

    @classmethod
    def sample(cls):
        result = {
            'code': 'yalda98',
            'count': 5,
            'start_date': '2020/12/2',
            'end_date': '2021/01/01',
            'percentage': 30,
            'minimum_order': 20000,
            'maximum_order': 300000
        }
        return cls(**result)
