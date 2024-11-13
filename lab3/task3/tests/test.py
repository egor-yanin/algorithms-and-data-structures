import unittest
from lab3.task3.src.main import pugalo_sort, task3
from lab3.utils import read_array, is_sorted, write_vars, read_str_lines


class TestCase(unittest.TestCase):

    def test_should_task3(self):
        data = read_array('../textsf/samples.txt', num=4, with_len=False)
        expected_result = ['NO', 'YES']

        print()
        for i in range(2):
            write_vars('../textsf/input.txt', data[i * 2], data[i * 2 + 1])
            task3()
            ans = read_str_lines('../textsf/output.txt')[0].strip()

            self.assertEqual(ans, expected_result[i])
