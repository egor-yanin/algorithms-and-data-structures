import unittest
from lab3.task5.src.main import task5
from lab3.utils import *
import os


current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../txtf/input.txt')
file_output = os.path.join(current_script_dir, '../txtf/output.txt')


class TestCase(unittest.TestCase):

    def test_h_index(self):
        path = os.path.join(current_script_dir, '../txtf/test.txt')
        n = read_int(path)
        for i in range(n):
            data = read_array(path, start=1 + i * 2, num=2, with_len=False)
            lst = data[0]
            expected_result = data[1][0]

            write_vars(file_input, lst)
            task5()
            result = read_int(file_output)

            self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        file_sample = os.path.join(current_script_dir, '../txtf/sample.txt')
        data_sample = read_str_lines(file_sample)
        write_vars(file_input, data_sample[0])
