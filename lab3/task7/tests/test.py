import unittest
from lab3.task7.src.main import *
import os


current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../txtf/input.txt')
file_output = os.path.join(current_script_dir, '../txtf/output.txt')


class Lab3Task7TestCase(unittest.TestCase):

    def test_should_radix_sort(self):
        # given
        test_file = os.path.join(current_script_dir, '../txtf/test.txt')
        expected_result = [1, 3, 5, 4, 2]
        n, m = read_array(test_file, with_len=False)[0]
        lst = read_str_lines(test_file, start=1, num=n)

        # when
        write_vars(file_input, [n, m, n-1], *lst)
        task7()
        res = read_array(file_output, with_len=False)[0]

        # then
        self.assertEqual(res, expected_result)

    @classmethod
    def tearDownClass(cls):
        file_sample = os.path.join(current_script_dir, '../txtf/sample.txt')
        data_sample = read_str_lines(file_sample)
        write_vars(file_input, *data_sample)
