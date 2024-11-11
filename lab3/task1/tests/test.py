from lab3.utils import *
from lab3.task1.src.main import *
import unittest

FILES = ['worst_case.txt', 'average_case.txt', 'best_case.txt']


class TestCase(unittest.TestCase):

    def test_partition3(self):
        a1 = read_array('../xtxt/partition3test.txt')[0][0]
        m1, m2 = partition3(a1, 0, len(a1) - 1)
        self.assertEqual([m1, m2], [3, 5])
        self.assertEqual(a1, [1, 2, 1, 3, 3, 3, 5, 4])

    def test_quick_sort(self):
        for file in FILES:
            for a, n in read_array(f'../xtxt/{file}', num=2, with_len=True):
                write_vars('../xtxt/input.txt', n, a)
                print('Файл', file)
                print('Массив размера', n)
                main()
                a = read_array('../xtxt/output.txt', with_len=False)
                self.assertTrue(is_sorted(a))
