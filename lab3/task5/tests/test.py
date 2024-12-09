import unittest
from lab3.task5.src.main import task5
from lab3.utils import *
import os


current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../txtf/input.txt')
file_output = os.path.join(current_script_dir, '../txtf/output.txt')


class Lab3Task5TestCase(unittest.TestCase):

    def test_h_index(self):
        # given
        path = os.path.join(current_script_dir, '../txtf/test.txt')
        data = read_array(path, with_len=False)[0]
        expected_result = 5

        # when
        write_vars(file_input, data)
        task5()
        result = read_int(file_output)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        file_sample = os.path.join(current_script_dir, '../txtf/sample.txt')
        data_sample = read_str_lines(file_sample)
        write_vars(file_input, data_sample[0])
