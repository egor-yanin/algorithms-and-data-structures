from lab5.task6.src.main import LowerHeap, LowerPriorityQueue
import unittest


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

    def test_should_insert_queue(self):
        # given
        queue = LowerPriorityQueue()
        expected_result = [13]

        # when
        queue.insert(13)
        result = queue.get_list()

        # then
        self.assertEqual(result, expected_result)

    def test_should_extract_min_queue(self):
        # given
        queue = LowerPriorityQueue()
        expected_result = 13

        # when
        queue.insert(52)
        queue.insert(134)
        queue.insert(13)
        result = queue.extract_min()

        # then
        self.assertEqual(result, expected_result)

    def test_should_decrease_key_queue(self):
        # given
        queue = LowerPriorityQueue()
        expected_result = 12

        # when
        queue.insert(52)
        queue.insert(134)
        queue.insert(13)
        queue.decrease_key(queue.get_index(134), 12)
        result = queue.extract_min()

        # then
        self.assertEqual(result, expected_result)
