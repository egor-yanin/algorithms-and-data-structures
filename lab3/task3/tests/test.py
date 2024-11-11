import unittest
from lab3.task3.src.main import *
from lab3.utils import *


class TestCase(unittest.TestCase):

    def test_sample(self):
        fin = read_array('../xtxt/samples.txt', num=4, with_len=False)
        ans = [False, True]
        print()
        for i in range(2):
            l, k = fin[i*2]
            lst = fin[i*2 + 1]
            pugalo_sort(lst, k)
            self.assertEqual(is_sorted(lst), ans[i])
