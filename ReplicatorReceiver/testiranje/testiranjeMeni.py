import unittest
from unittest import mock

import main
from assets.helper import CODE


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

    def test_po_vrednosti(self):
        with mock.patch('builtins.input', return_value="CODE_ANALOG"):
            assert main.iscitavanje_poslednje_vrednosti() == CODE.CODE_ANALOG.name

    def test_po_vrednosti_error(self):
        with mock.patch('builtins.input', return_value="SAD"):
            assert main.iscitavanje_poslednje_vrednosti() is None

    def test_po_vremenskom_intervalu_error(self):
        with mock.patch('builtins.input', return_value="DANAS"):
            assert main.iscitavanje_po_vr_intervalu() is None


if __name__ == '__main__':
    unittest.main()
