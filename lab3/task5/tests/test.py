import unittest
from lab3.task5.src.main import task5
from lab3.utils import *
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')
FILE_TEST = os.path.join(CURRENT_DIR, '../txtf/test.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab3Task5TestCase(unittest.TestCase):

    def test_should_h_index(self):
        # given
        data = read_array(FILE_TEST, with_len=False)[0]
        expected_result = 5

        # when
        write_vars(FILE_INPUT, data)
        task5()
        result = read_int(FILE_OUTPUT)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        data_sample = read_str_lines(FILE_SAMPLE)
        write_vars(FILE_INPUT, data_sample[0])
