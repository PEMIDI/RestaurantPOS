import inspect
import io
import random
import unittest

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
            self.assertEqual(_class.manager, None, "{} `manager` attribute is not None".format(_class))
            sample_1 = _class.sample()
            self.assertIsInstance(_class.manager, Manager, "{} `manager` is not initiating correctly".format(_class))
            self.assertTrue(hasattr(_class.manager, 'search'), "{} `manager` is not initiating correctly".format(_class))
            self.assertTrue(hasattr(_class.manager, '_class'), "{} `manager` is not initiating correctly".format(_class))
            sample_2 = _class.sample()
            self.assertEqual(sample_1, sample_2, "manager should not be propagated")

    def test_new_sample_methods(self):
        for _class in CLASSES:
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
        bills = [Bill.sample() for _ in range(20)]
        paid_bills = [bill.payment.pay() for bill in bills if random.choice([True, False])]
        unpaid_bills = filter(lambda x: not x.payment.is_paid, bills)
        self.assertListEqual(sorted(Bill.show_unpaid()), sorted(list(unpaid_bills)), ".show_unpaid() method is not working properly")
        self.assertListEqual(sorted(Bill.show_paid()), sorted(list(paid_bills)), ".show_paid() method is not working properly")

    def test_paid_payment_list(self):
        self.assertTrue(hasattr(Payment, 'paid_list'), "paid_list() method not implemented")
        payments = [Payment.sample(is_paid=random.choice([True, False])) for _ in range(10)]
        paid_list = filter(lambda x: x.payment.is_paid, payments)
        self.assertListEqual(sorted(Payment.paid_list()), sorted(list(paid_list)), ".show_paid() method is not working properly")
        self.assertEqual(sum([payment.price for payment in paid_list]), Payment.total_paid(), ".total_paid() is not calculated correctly")


class MenuClassChecks(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_item_stdout(self, mock_stdout):
        Item.show_menu()
        self.assertIsNotNone(mock_stdout.getvalue(), "show_menu() returns nothing")
