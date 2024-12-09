from lab5.task4.src.main import LowerHeap
from lab5.utils import write_vars, read_lines
import os
import unittest


current_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_dir, '../txtf/input.txt')


class Lab5Task6TestCase(unittest.TestCase):
    def test_should_max_heapify(self):
        # given
        lst = [34, 23, 45, 52, 13]
        expected_result = [13, 23, 45, 52, 34]

        # when
        heap = LowerHeap(lst)
        result = heap.get_list()

        # then
        self.assertEqual(result, expected_result)

    def test_should_create_lower_heap(self):
        # given
        lst = [34, 52, 45, 23, 13]
        expected_result = [13, 23, 45, 34, 52]

        # when
        heap = LowerHeap(lst)
        result = heap.get_list()

        # then
        self.assertEqual(result, expected_result)

    def test_should_get_swaps(self):
        # given
        lst = [5, 4, 3, 2, 1]
        expected_result = [(1, 4), (0, 1), (1, 3)]

        # when
        heap = LowerHeap(lst)
        result = heap.get_swaps()

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        file_sample = os.path.join(current_dir, '../txtf/sample.txt')
        write_vars(file_input, *read_lines(file_sample))
