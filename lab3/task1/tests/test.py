from lab3.utils import read_array, is_sorted, write_vars
from lab3.task1.src.main import partition3, task1, quick_sort, randomized_quick_sort
import unittest


class TestCase(unittest.TestCase):

    def test_should_partition3(self):
        expected_partition = [3, 5]
        expected_result = [1, 2, 1, 3, 3, 3, 5, 4]

        a1 = read_array('../xtxt/partition3test.txt')[0][0]
        m1, m2 = partition3(a1, 0, len(a1) - 1)

        self.assertEqual([m1, m2], expected_partition)
        self.assertEqual(a1, expected_result)

    def test_should_randomized_quick_sort(self):
        files = ['worst_case.txt', 'average_case.txt', 'best_case.txt']

        for f in files:
            for a, n in read_array(f'../xtxt/{f}', num=2, with_len=True):
                write_vars('../xtxt/input.txt', n, a)
                print('Файл', f)
                print('Массив размера', n)
                task1()
                a = read_array('../xtxt/output.txt', with_len=False)

                self.assertTrue(is_sorted(a))

    def test_should_quick_sort(self):
        files = ['worst_case.txt', 'average_case.txt', 'best_case.txt']

        for f in files:
            for a, n in read_array(f'../xtxt/{f}', num=2, with_len=True):
                print()
                print('Файл', f)
                print('Массив размера', n)
                quick_sort(a, 0, len(a) - 1)

                self.assertTrue(is_sorted(a))
