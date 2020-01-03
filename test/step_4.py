import unittest


class CheckFunctionExistence(unittest.TestCase):
    def test_step_functions_existence(self):
        from utils import get_order, show_unpaid_bill, pay_bill, get_finance_report
        try:
            from utils import create_time
        except:
            from utils import create_item