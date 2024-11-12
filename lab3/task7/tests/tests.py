import unittest
from lab3.task7.src.main import *


class TestCase(unittest.TestCase):

    def test_radix_sort(self):
        test_file = '../xtxt/test.txt'
        fin = '../xtxt/input.txt'
        print()
        ans = [[1, 2, 3, 4, 5], [5, 2, 1, 4, 3], [1, 4, 5, 2, 3], [1, 4, 3, 2, 5], [1, 3, 5, 4, 2]]
        n, m = read_array(test_file, with_len=False)[0]
        lst = read_str_lines(test_file, start=1, num=n)
        for phase in range(m + 1):
            write_vars(fin, [n, m, phase], *lst)
            main()
            res = read_array('../xtxt/output.txt', with_len=False)[0]
            self.assertEqual(res, ans[phase])
