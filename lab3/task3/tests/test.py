import unittest
from lab3.task3.src.main import task3
from lab3.utils import read_array, write_vars, read_str_lines
import os


current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../txtf/input.txt')
file_output = os.path.join(current_script_dir, '../txtf/output.txt')


class TestCase(unittest.TestCase):

    def test_should_task3(self):
        path = os.path.join(current_script_dir, '../txtf/samples.txt')
        data = read_array(path, num=4, with_len=False)
        expected_result = ['NO', 'YES']

        print()
        for i in range(2):
            write_vars(file_input, data[i * 2], data[i * 2 + 1])
            task3()
            ans = read_str_lines(file_output)[0].strip()

            self.assertEqual(ans, expected_result[i])
