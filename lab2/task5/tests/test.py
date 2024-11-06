from lab2.task5.src.main import main
from lab2.utils import read_int
import psutil
import time
import unittest


class TestCaseTask5(unittest.TestCase):

    def test_true(self):
        start = time.perf_counter()
        main('true.txt')
        print(f'\nЗатрачено времени: {round(time.perf_counter() - start, 6)} c.')
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
        flag = bool(read_int('output.txt'))
        self.assertTrue(flag)

    def test_false(self):
        start = time.perf_counter()
        main('false.txt')
        print(f'\nЗатрачено времени: {round(time.perf_counter() - start, 6)} c.')
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
        flag = bool(read_int('output.txt'))
        self.assertFalse(flag)
