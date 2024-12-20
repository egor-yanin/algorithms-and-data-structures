from lab3.utils import read_array, is_sorted, write_vars
from lab3.task1.src.main import partition3, task1, quick_sort, randomized_quick_sort
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')
FILE_TEST = os.path.join(CURRENT_DIR, '../txtf/partition3test.txt')
FILE_WORST = os.path.join(CURRENT_DIR, '../txtf/worst_case.txt')
FILE_AVERAGE = os.path.join(CURRENT_DIR, '../txtf/average_case.txt')
FILE_BEST = os.path.join(CURRENT_DIR, '../txtf/best_case.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab3Task1TestCase(unittest.TestCase):

    def test_should_partition3(self):
        # given
        expected_partition = [3, 5]
        expected_result = [1, 2, 1, 3, 3, 3, 5, 4]
        path = FILE_TEST

        # when
        a1 = read_array(path)[0][0]
        m1, m2 = partition3(a1, 0, len(a1) - 1)

        # then
        self.assertEqual([m1, m2], expected_partition)
        self.assertEqual(a1, expected_result)

    def test_should_randomized_quick_sort_worst_case(self):
        # given
        path = FILE_WORST
        lst = read_array(path, with_len=True)[0][0]

        # when
        randomized_quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    def test_should_randomized_quick_sort_average_case(self):
        # given
        path = FILE_AVERAGE
        lst = read_array(path, with_len=True)[0][0]

        # when
        randomized_quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    def test_should_randomized_quick_sort_best_case(self):
        # given
        path = FILE_BEST
        lst = read_array(path, with_len=True)[0][0]

        # when
        randomized_quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    def test_should_quick_sort_worst_case(self):
        # given
        path = FILE_WORST
        lst = read_array(path, with_len=True)[0][0]

        # when
        quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    def test_should_quick_sort_average_case(self):
        # given
        path = FILE_AVERAGE
        lst = read_array(path, with_len=True)[0][0]

        # when
        quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    def test_should_quick_sort_best_case(self):
        # given
        path = FILE_BEST
        lst = read_array(path, with_len=True)[0][0]

        # when
        quick_sort(lst)

        # then
        self.assertTrue(is_sorted(lst))

    @classmethod
    def tearDownClass(cls):
        data_sample = read_array(FILE_SAMPLE)
        write_vars(FILE_INPUT, *data_sample[0][::-1])
