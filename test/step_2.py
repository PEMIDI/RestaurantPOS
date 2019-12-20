import inspect
import unittest
import uuid

from finance import Bill, Payment
from menu import Item
from order import Order
from saloon import Table
from discount import Discount


class ConstructorValidatorTest(unittest.TestCase):
    _classes = [Payment, Bill, Item, Order, Table]

    def test_uuid_initialization(self):
        for _class in self._classes:
            sample = _class.sample()
            self.assertTrue(hasattr(sample, 'uuid'), 'uuid not implemented in {} class'.format(_class))
            self.assertIsInstance(sample.uuid, uuid.UUID, 'uuid value is not correct in {} class sample'.format(_class))

    def test_initialization_date(self):
        for _class in self._classes:
            signature = inspect.signature(_class)
            existence = [attr in list(signature.parameters) for attr in ['uuid', 'datetime']]
            self.assertFalse(any(existence), "uuid or datetime attrs should not be accessible from __init__")


class TestItemClass(unittest.TestCase):

    def setUp(self):
        self.item = Item.sample()

    def test_item_class_initialization(self):
        self.assertTrue(hasattr(self.item, 'item_id'), "Item has no attr item_id")
        item_2 = Item.sample()
        self.assertTrue((item_2.item_id - self.item.item_id) == 1, "item_id is not incremental")

    def check_jalali_datetime(self):
        from khayyam import JalaliDatetime
        self.assertTrue(hasattr(self.item, 'jalali_datetime'), "jalali_datetime property is not added to the Item class")
        self.assertIsInstance(type(self.item).jalali_datetime, property, 'jalali_datetime should be method')
        self.assertIsInstance(self.item.jalali_datetime, JalaliDatetime, 'jalali_datetime property is not returning correct value')


class TestOrderClass(unittest.TestCase):

    def setUp(self):
        self.order = Order.sample()
        self.item_1 = Item.sample()
        self.item_1.price = 2000
        self.item_2 = Item.sample()
        self.item_2.price = 10000
        self.item_3 = Item.sample()
        self.item_3.price = 15000
        self.table = Table.sample()

    def test_updated_attrs(self):
        existence = ['orders_list', 'un_paid_orders', 'assign_table', 'set_bill']
        self.assertTrue(all(existence), "Order class attrs and methods are not complete")

    def test_order_initialization(self):
        items = {self.item_1: 2, self.item_2:1, self.item_3: 1}
        order = Order(item_dict=items, in_out='I', table=self.table)
        self.assertIsInstance(order.bill, Bill, 'Bill instance is not created successfully')
        items_price = sum(map(lambda x: x.price * items[x], items))
        self.assertEqual(order.bill.total_price, items_price, 'total_price is not True in bill')


class TestDiscountClass(unittest.TestCase):

    def test_all_attrs(self):
        attrs = ['code', 'count', 'start_date', 'end_date', 'percentage', 'minimum_order', 'maximum_order']
        self.assertTrue(hasattr(Discount, 'sample'), "sample method not implemented in Discount class")
        discount = Discount.sample()
        for attr in attrs:
            self.assertTrue(hasattr(discount, attr), 'discount objects has no attr called {}'.format(attr))
