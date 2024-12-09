import unittest
from lab3.task3.src.main import task3
from lab3.utils import read_array, write_vars, read_str_lines
import os


current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../txtf/input.txt')
file_output = os.path.join(current_script_dir, '../txtf/output.txt')


class Lab3Task3TestCase(unittest.TestCase):

    def test_should_task3(self):
        # given
        path = os.path.join(current_script_dir, '../txtf/test_data.txt')
        data = read_array(path, num=2, with_len=False)
        expected_result = 'YES'

        # when
        write_vars(file_input, data[0], data[1])
        task3()
        ans = read_str_lines(file_output, num=1)[0].strip()

        # then
        self.assertEqual(ans, expected_result)

    @classmethod
    def tearDownClass(cls):
        file_sample = os.path.join(current_script_dir, '../txtf/sample')
        data_sample = read_array(file_sample, with_len=False, num=2)
        write_vars(file_input, *data_sample)
