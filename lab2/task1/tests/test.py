import unittest
from lab2.task1.src.main import merge_sort
from lab2.utils import read_array, is_sorted, write_vars
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')
FILE_RAND = os.path.join(CURRENT_DIR, '../txtf/rand.txt')
FILE_REVERSE = os.path.join(CURRENT_DIR, '../txtf/rev.txt')
FILE_SORTED = os.path.join(CURRENT_DIR, '../txtf/sort.txt')


class Lab2Task1TestCase(unittest.TestCase):
    def test_should_merge_sort_reversed_file(self):
        # given
        lst = read_array(FILE_REVERSE)[0][0]

        # when
        result = merge_sort(lst)

        # then
        self.assertTrue(is_sorted(result))

    def test_should_merge_sort_sorted_file(self):
        # given
        lst = read_array(FILE_SORTED)[0][0]

        # when
        result = (merge_sort(lst))

        # then
        self.assertTrue(is_sorted(result))

    def test_should_merge_sort_randomized_file(self):
        # given
        lst = read_array(FILE_RAND)[0][0]

        # when
        result = merge_sort(lst)

        # then
        self.assertTrue(is_sorted(result))

    @classmethod
    def tearDownClass(cls):
        lst, length = read_array(FILE_SAMPLE)[0]
        write_vars(FILE_INPUT, length, lst)
