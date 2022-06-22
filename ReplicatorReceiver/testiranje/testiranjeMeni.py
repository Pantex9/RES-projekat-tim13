import unittest
from unittest import mock

import main


class MyTestCase(unittest.TestCase):

    def test_Meni_case1(self):
        with mock.patch('builtins.input', return_value="1"):
            assert main.Meni() == 1

    def test_Meni_case2(self):
        with mock.patch('builtins.input', return_value="7"):
            assert main.Meni() is None
        with mock.patch('builtins.input', return_value="-2"):
            assert main.Meni() is None

    def test_Meni_case3(self):
        with mock.patch('builtins.input', return_value="test"):
            assert main.Meni() is None
        with mock.patch('builtins.input', return_value=[]):
            assert main.Meni() is None


if __name__ == '__main__':
    unittest.main()
