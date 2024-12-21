import unittest
from lab3.task7.src.main import *
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')
FILE_TEST = os.path.join(CURRENT_DIR, '../txtf/test.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab3Task7TestCase(unittest.TestCase):

    def test_should_radix_sort(self):
        # given
        expected_result = [1, 3, 5, 4, 2]
        n, m = read_array(FILE_TEST, with_len=False)[0]
        lst = read_str_lines(FILE_TEST, start=1, num=n)

        # when
        write_vars(FILE_INPUT, [n, m, n - 1], *lst)
        task7()
        res = read_array(FILE_OUTPUT, with_len=False)[0]

        # then
        self.assertEqual(res, expected_result)

    @classmethod
    def tearDownClass(cls):
        data_sample = read_str_lines(FILE_SAMPLE)
        write_vars(FILE_INPUT, *data_sample)
