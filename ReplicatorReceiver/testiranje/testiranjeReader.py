import unittest
from unittest.mock import patch, mock_open
from assets.helper import DeltaCD
from ReplicatorReceiver.Reader import Reader


class TestFileWriter(unittest.TestCase):
    def test_file_writer(self):
        fake_file_path ="fake/file/path"
        content = DeltaCD(55)
        with patch('ReplicatorReceiver.Reader.open', mock_open()) as mocked_file:
            Reader("test1").write_in_file_pr(fake_file_path, content)

            # assert if opened file on write mode 'w'
            mocked_file.assert_any_call(fake_file_path, 'a')

            # assert if write(content) was called from the file opened
            # in another words, assert if the specific content was written in file
            mocked_file().write.assert_called_once_with(content)


if __name__ == '__main__':
    unittest.main()
