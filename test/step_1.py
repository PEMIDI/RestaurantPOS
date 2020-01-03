import unittest

from finance import Bill, Payment
from menu import Item
from order import Order
from saloon import Table
from user import Supervisor

ATTRS = {
    Supervisor: ['username', 'password', 'phone_number'],
    Item: ['uuid', 'name', 'price', 'item_type', 'datetime',
           'food_list', 'beverage_list', 'starter_list'],
    Bill: ['uuid', 'total_price', 'payment'],
    Order: ['uuid', 'item_dict', 'in_out', 'datetime', 'bill', 'table'],
    Payment: ['uuid', 'payment_type', 'is_paid', 'datetime', 'price'],
    Table: ['uuid', 'number', 'capacity', 'reserved', 'is_available',
            'table_list']
}


class CheckAllClassDefinition(unittest.TestCase):

    def test_sample_method(self):
        for _class in ATTRS.keys():
            self.assertTrue(hasattr(_class, 'sample'))
            sample = _class.sample()
            self.assertIsNotNone(sample, 'Sample is None')
            self.assertIsInstance(sample, _class)

    def test_class_attrs(self):
        for _class in ATTRS:
            sample = _class.sample()
            for attr in ATTRS[_class]:
                self.assertTrue(hasattr(sample, attr))
