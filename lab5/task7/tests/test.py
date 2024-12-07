from lab5.task7.src.main import heap_sort
from lab5.utils import is_sorted
import unittest
import random


class Lab5Task7TestCase(unittest.TestCase):
    def test_should_heap_sort_worst_case(self):
        # given
        random_numbers = sorted(random.randint(-10**9, 10**9) for _ in range(10000))

        # when
        result = heap_sort(random_numbers)

        # then
        self.assertTrue(is_sorted(result, reverse=True))

    def test_should_heap_sort_average_case(self):
        # given
        random_numbers = [random.randint(-10**9, 10**9) for _ in range(10000)]

        # when
        result = heap_sort(random_numbers)

        # then
        self.assertTrue(is_sorted(result, reverse=True))

    def test_should_heap_sort_best_case(self):
        # given
        random_numbers = sorted([random.randint(-10 ** 9, 10 ** 9) for _ in range(10000)], reverse=True)

        # when
        result = heap_sort(random_numbers)

        # then
        self.assertTrue(is_sorted(result, reverse=True))
