from lab3.utils import read_array, is_sorted, write_vars
from lab3.task1.src.main import partition3, task1, quick_sort, randomized_quick_sort
import unittest
import os


current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../txtf/input.txt')
file_output = os.path.join(current_script_dir, '../txtf/output.txt')


class Lab3Task1TestCase(unittest.TestCase):

    def test_should_partition3(self):
        # given
        expected_partition = [3, 5]
        expected_result = [1, 2, 1, 3, 3, 3, 5, 4]
        file = os.path.join(current_script_dir, '../txtf/partition3test.txt')

        # when
        a1 = read_array(file)[0][0]
        m1, m2 = partition3(a1, 0, len(a1) - 1)

        # then
        self.assertEqual([m1, m2], expected_partition)
        self.assertEqual(a1, expected_result)

    def test_should_randomized_quick_sort_worst_case(self):
        # given
        path = os.path.join(current_script_dir, '../txtf/worst_case.txt')
        lst = read_array(path, with_len=True)[0][0]

        # when
        randomized_quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    def test_should_randomized_quick_sort_average_case(self):
        # given
        path = os.path.join(current_script_dir, '../txtf/average_case.txt')
        lst = read_array(path, with_len=True)[0][0]

        # when
        randomized_quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    def test_should_randomized_quick_sort_best_case(self):
        # given
        path = os.path.join(current_script_dir, '../txtf/best_case.txt')
        lst = read_array(path, with_len=True)[0][0]

        # when
        randomized_quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    def test_should_quick_sort_worst_case(self):
        # given
        path = os.path.join(current_script_dir, '../txtf/worst_case.txt')
        lst = read_array(path, with_len=True)[0][0]

        # when
        quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    def test_should_quick_sort_average_case(self):
        # given
        path = os.path.join(current_script_dir, '../txtf/average_case.txt')
        lst = read_array(path, with_len=True)[0][0]

        # when
        quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    def test_should_quick_sort_best_case(self):
        # given
        path = os.path.join(current_script_dir, '../txtf/best_case.txt')
        lst = read_array(path, with_len=True)[0][0]

        # when
        quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    @classmethod
    def tearDownClass(cls):
        file_sample = os.path.join(current_script_dir, '../txtf/sample.txt')
        data_sample = read_array(file_sample)
        write_vars(file_input, *data_sample[0][::-1])
