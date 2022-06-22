import unittest
from ReplicatorReceiver import Receiver
from unittest.mock import MagicMock, patch

from ReplicatorReceiver.Receiver import ReplicatorReceiver
from assets.helper import ReceiverProperty, CODE, DeltaCD


class MyTestCase(unittest.TestCase):
    # TESTOVI
    def test_clear_delta_cd(self):
        rr = ReplicatorReceiver()
        dcd = DeltaCD(55)
        dcd.add = [1, 2, 3]
        dcd.update = [4, 5, 6]
        rr.clear_delta_cd(delta_cd=dcd)
        self.assertCountEqual([], dcd.add)
        self.assertCountEqual([], dcd.update)

    def test_check_delta_size(self):
        rr = ReplicatorReceiver()
        dcd_true1 = DeltaCD(55)
        dcd_true1.add = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        dcd_true1.update = []
        dcd_true2 = DeltaCD(55)
        dcd_true2.add = []
        dcd_true2.update = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        dcd_true3 = DeltaCD(55)
        dcd_true3.add = [1, 2, 3, 4, 5]
        dcd_true3.update = [1, 2, 3, 4, 5]
        dcd_false1 = DeltaCD(55)
        dcd_false1.add = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        dcd_false1.update = []
        dcd_false2 = DeltaCD(55)
        dcd_false2.add = []
        dcd_false2.update = []

        self.assertEqual(rr.check_delta_size(dcd_true1), True)
        self.assertEqual(rr.check_delta_size(dcd_true2), True)
        self.assertEqual(rr.check_delta_size(dcd_true3), True)
        self.assertEqual(rr.check_delta_size(dcd_false1), False)
        self.assertEqual(rr.check_delta_size(dcd_false2), False)

    def test_check_if_empty(self):
        rr = ReplicatorReceiver()
        empty_list = []
        list_with_elements = [1, 2]
        result_true = rr.check_if_empty(empty_list)
        result_false = rr.check_if_empty(list_with_elements)

        self.assertEqual(result_true, True)
        self.assertEqual(result_false, False)


    def test_check_code_digital(self):
        rr = ReplicatorReceiver()
        rp_true = ReceiverProperty(CODE.CODE_DIGITAL, 500)
        rp_false = ReceiverProperty(CODE.CODE_ANALOG, 500)
        result_true = rr.check_code_digital(rp=rp_true)
        result_false = rr.check_code_digital(rp=rp_false)

        self.assertEqual(result_true, True)
        self.assertEqual(result_false, False)

    def test_two_percent(self):
        rr = ReplicatorReceiver()
        result = rr.two_percent(50)

        self.assertEqual(result, 1)
        self.assertRaises(ValueError, rr.two_percent, 0)

    def test_deadband(self):
        rr = ReplicatorReceiver()
        result_true1 = rr.deadband(100, 103)
        result_false1 = rr.deadband(100, 102)
        result_true2 = rr.deadband(100, 97)
        result_false2 = rr.deadband(100, 98)

        self.assertEqual(result_true1, True)
        self.assertEqual(result_true2, True)
        self.assertEqual(result_false1, False)
        self.assertEqual(result_false2, False)

if __name__ == '__main__':
    unittest.main()