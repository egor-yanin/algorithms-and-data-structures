import unittest
from lab3.task7.src.main import *
import os


current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../txtf/input.txt')
file_output = os.path.join(current_script_dir, '../txtf/output.txt')


class TestCase(unittest.TestCase):

    def test_should_radix_sort(self):
        test_file = os.path.join(current_script_dir, '../txtf/test.txt')
        expected_result = [[1, 2, 3, 4, 5], [5, 2, 1, 4, 3], [1, 4, 5, 2, 3], [1, 4, 3, 2, 5], [1, 3, 5, 4, 2]]
        n, m = read_array(test_file, with_len=False)[0]
        lst = read_str_lines(test_file, start=1, num=n)

        print()
        for phase in range(m + 1):
            write_vars(file_input, [n, m, phase], *lst)
            task7()
            res = read_array(file_output, with_len=False)[0]
            self.assertEqual(res, expected_result[phase])
