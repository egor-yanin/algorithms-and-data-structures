import unittest
from lab5.task1.src.main import is_correct_node, is_heap


class Lab5Task1TestCase(unittest.TestCase):
    def test_should_is_correct_node(self):
        # given
        heap_1 = [0, 1, 3, 2, 4, 5]
        heap_2 = [0, 2, 1, 3, 0, 1]
        expected_result = [True, False]

        # when
        result = [is_correct_node(heap_1, 1), is_correct_node(heap_2, 1)]

        # then
        self.assertEqual(result, expected_result)

    def test_should_is_heap(self):
        # given
        heap_1 = [1, 3, 2, 4, 5]
        heap_2 = [2, 1, 3, 2, 4, 4, 5]
        expected_result = [True, False]

        # when
        result = [is_heap(heap_1), is_heap(heap_2)]

        # then
        self.assertEqual(result, expected_result)
