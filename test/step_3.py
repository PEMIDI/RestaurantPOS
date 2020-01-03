import inspect
import io
import random
import unittest
import unittest.mock

from discount import Discount
from finance import Bill, Payment
from menu import Item
from order import Order
from saloon import Table
from user import Supervisor
from lib import Manager

CLASSES = {Supervisor, Item, Bill, Order, Payment, Table, Discount}


class CommonClassChecks(unittest.TestCase):
    def test_list_class_attr(self):
        for _class in CLASSES:
            objects_list = _class.__name__.lower() + "_list"
            self.assertTrue(hasattr(_class, objects_list), "{} has not objects list".format(_class))
            self.assertTrue(hasattr(_class, 'manager'), "{} has not attribute `manager`".format(_class))
            instance_list = getattr(_class, '{}_list'.format(_class.__name__.lower()))
            if not len(instance_list):
                self.assertEqual(_class.manager, None, "{} `manager` attribute is not None".format(_class))
            sample_1 = _class.sample()
            self.assertIsInstance(_class.manager, Manager, "{} `manager` is not initiating correctly".format(_class))
            self.assertTrue(hasattr(_class.manager, 'search'), "{} `manager` is not initiating correctly".format(_class))
            self.assertTrue(hasattr(_class.manager, '_class'), "{} `manager` is not initiating correctly".format(_class))
            sample_2 = _class.sample()
            self.assertEqual(sample_1.manager, sample_2.manager, "manager should not be propagated")

    def test_new_sample_methods(self):
        for _class in CLASSES:
            if _class == Bill:
                continue
            signature = inspect.signature(_class.sample)
            self.assertGreater(len(list(signature.parameters)), 1, "Refactor your {} sample class according to TODO-3".format(_class))


class FinanceChecks(unittest.TestCase):
    def test_payment_objects_inside_bill(self):
        bill = Bill.sample()
        self.assertTrue(hasattr(bill, 'payment'), "Bill instance has not attribute payment")
        self.assertIsInstance(bill.payment, Payment, "bill.payment is not initiated correctly")
        self.assertTrue(hasattr(bill.payment, 'pay'), "Payment instance has not pay() method")
        self.assertTrue(hasattr(bill.payment, 'total_paid'), "Payment instance has not total_paid() method")

    def test_unpaid_bill_list(self):
        self.assertTrue(hasattr(Bill, 'show_unpaid'), "show_unpaid() method not implemented")
        self.assertTrue(hasattr(Bill, 'show_paid'), "show_paid() method not implemented")
        unpaid_bills = list(Bill.show_unpaid())
        paid_bills = list(Bill.show_paid())
        new_bills = [Bill.sample() for _ in range(2)]
        new_paid_bills = [bill for bill in new_bills if random.choice([True, False])]
        _ = list(map(lambda bill: bill.payment.pay(), new_paid_bills))
        unpaid_bills.extend(list(filter(lambda x: not x.payment.is_paid, new_bills)))
        paid_bills.extend(new_paid_bills)
        self.assertListEqual(sorted(Bill.show_unpaid(), key=lambda x: x.uuid), sorted(list(unpaid_bills), key=lambda x: x.uuid), ".show_unpaid() method is not working properly")
        self.assertListEqual(sorted(Bill.show_paid(), key=lambda x: x.uuid), sorted(list(paid_bills), key=lambda x: x.uuid), ".show_paid() method is not working properly")

    def test_paid_payment_list(self):
        self.assertTrue(hasattr(Payment, 'paid_list'), "paid_list() method not implemented")
        payments = [Payment.sample(is_paid=random.choice([True, False])) for _ in range(10)]
        paid_list = list(filter(lambda x: x.is_paid, payments))
        self.assertListEqual(sorted(Payment.paid_list(), key=lambda x: x.uuid), sorted(list(paid_list), key=lambda x: x.uuid), ".show_paid() method is not working properly")
        self.assertEqual(sum([payment.price for payment in paid_list]), Payment.total_paid(), ".total_paid() is not calculated correctly")


class MenuClassChecks(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_item_stdout(self, mock_stdout):
        Item.show_menu()
        self.assertNotEqual(mock_stdout.getvalue(), '', "show_menu() returns nothing")
