import unittest
from ReplicatorReceiver.Logger import Logger
from unittest.mock import patch, mock_open
from assets.helper import CODE
from datetime import datetime


class TestFileWriter(unittest.TestCase):

    def test_file_writer(self):
        fake_file_path = "fake/file/path"
        content = "sdadasdada"
        with patch('ReplicatorReceiver.Logger.open', mock_open()) as mocked_file:
            Logger("milos").write_in_file(fake_file_path, content)

            # assert if opened file on write mode 'w'
            mocked_file.assert_called_once_with(fake_file_path, 'a')

            # assert if write(content) was called from the file opened
            # in another words, assert if the specific content was written in file
            mocked_file().write.assert_called_once_with(content)

    def test_logg_send_codes(self):
        test_code = CODE(CODE.CODE_ANALOG)
        test_value = 1111
        test_value1 = -1111
        test_datetime = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        test_writerid = 111
        test_writerid1 = -111

        self.assertEqual(None, Logger.LoggSentCodes(Logger("TestiranjeLOGGER\\test1"), test_code, test_value, test_datetime, test_writerid))
        self.assertRaises(Exception, Logger.LoggSentCodes(Logger("TestiranjeLOGGER\\test1"), test_code, test_value1, test_datetime, test_writerid))
        self.assertRaises(Exception, Logger.LoggSentCodes(Logger("TestiranjeLOGGER\\test1"), test_code, test_value, test_datetime, test_writerid1))
        self.assertRaises(Exception, Logger.LoggSentCodes(Logger("TestiranjeLOGGER\\test1"), test_code, test_value1, test_datetime, test_writerid1))

    def test_logg_stored_codes(self):
        test_code = CODE(CODE.CODE_ANALOG)
        test_value = 1111
        test_value1 = -1111
        test_datetime = datetime.now().strftime("%d-%m-%y %H:%M:%S")

        self.assertEqual(None, Logger.LoggStoredCodes(Logger("TestiranjeLOGGER\\test2"), test_code, test_value, test_datetime))

        self.assertRaises(Exception, Logger.LoggStoredCodes(Logger("TestiranjeLOGGER\\test2"), test_code, test_value1, test_datetime))

    def test_logg_activity(self):
        test_activity = "sasdasa"
        test_activity1 = ""
        test_datetime = datetime.now().strftime("%d-%m-%y %H:%M:%S")

        self.assertEqual(None, Logger.LoggActivity(Logger("TestiranjeLOGGER\\test3"), test_activity, test_datetime))

        self.assertRaises(Exception, Logger.LoggActivity(Logger("TestiranjeLOGGER\\test3"), test_activity1, test_datetime))


if __name__ == '__main__':
    unittest.main()
