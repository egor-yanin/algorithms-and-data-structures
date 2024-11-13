import unittest
from lab3.task5.src.main import task5
from lab3.utils import *


class TestCase(unittest.TestCase):

    def test_h_index(self):
        n = read_int('../xtxt/test.txt')
        for i in range(n):
            data = read_array('../xtxt/test.txt', start=1+i*2, num=2, with_len=False)
            lst = data[0]
            expected_result = data[1][0]

            write_vars('../xtxt/input.txt', lst)
            task5()
            result = read_int('../xtxt/output.txt')

            self.assertEqual(result, expected_result)
