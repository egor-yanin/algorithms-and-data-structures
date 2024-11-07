from lab3.utils import *
from lab3.task1.src.main import *
import unittest
import math


class TestCase(unittest.TestCase):

    def test_partition3(self):
        a1 = read_array('partition3test.txt')[0][0]
        m1, m2 = partition3(a1, 0, len(a1) - 1)
        self.assertEqual([m1, m2], [3, 5])
        self.assertEqual(a1, [1, 2, 1, 3, 3, 3, 5, 4])
