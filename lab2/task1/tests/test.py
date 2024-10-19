import unittest
from lab2.task1.src.main import main
import psutil
import time
from random import randint


class TestCaseTask1(unittest.TestCase):

    def test_sample(self):
        start = time.perf_counter()
        main('input.txt')
        print(f'\nЗатрачено времени: {round(time.perf_counter() - start, 6)} c.')
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
        with open('input.txt') as f:
            lst = [int(x) for x in f.readlines()[1].split()]
        with open('output.txt') as f:
            self.assertEqual(f.readline().strip(), ' '.join([str(x) for x in sorted(lst)]))

    def test_reversed(self):
        start = time.perf_counter()
        main('rev.txt')
        print(f'\nЗатрачено времени: {round(time.perf_counter() - start, 6)} c.')
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
        with open('rev.txt') as f:
            f.seek(1)
            lst = [int(x) for x in f.readlines()[1].split()]
        with open('output.txt') as f:
            self.assertEqual(f.readline().strip(), ' '.join([str(x) for x in sorted(lst)]))

    def test_sorted(self):
        start = time.perf_counter()
        main('sort.txt')
        print(f'\nЗатрачено времени: {round(time.perf_counter() - start, 6)} c.')
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
        with open('sort.txt') as f:
            f.seek(1)
            lst = [int(x) for x in f.readlines()[1].split()]
        with open('output.txt') as f:
            self.assertEqual(f.readline().strip(), ' '.join([str(x) for x in sorted(lst)]))

    def test_rand(self):
        start = time.perf_counter()
        main('rand.txt')
        print(f'\nЗатрачено времени: {round(time.perf_counter() - start, 6)} c.')
        print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
        with open('rand.txt') as f:
            f.seek(1)
            lst = [int(x) for x in f.readlines()[1].split()]
        with open('output.txt') as f:
            self.assertEqual(f.readline().strip(), ' '.join([str(x) for x in sorted(lst)]))
