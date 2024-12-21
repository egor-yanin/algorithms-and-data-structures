import unittest
from lab3.task3.src.main import task3
from lab3.utils import read_array, write_vars, read_str_lines
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')
FILE_TEST = os.path.join(CURRENT_DIR, '../txtf/test.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab3Task3TestCase(unittest.TestCase):

    def test_should_task3(self):
        # given
        data = read_array(FILE_TEST, num=2, with_len=False)
        expected_result = 'YES'

        # when
        write_vars(FILE_INPUT, data[0], data[1])
        task3()
        ans = read_str_lines(FILE_OUTPUT, num=1)[0].strip()

        # then
        self.assertEqual(ans, expected_result)

    @classmethod
    def tearDownClass(cls):
        data_sample = read_array(FILE_SAMPLE, with_len=False, num=2)
        write_vars(FILE_INPUT, *data_sample)
