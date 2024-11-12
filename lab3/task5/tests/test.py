import unittest
from lab3.task5.src.main import h_index


class TestCase(unittest.TestCase):

    def test_h_index(self):
        print()
        self.assertEqual(h_index([0, 0, 0, 1000, 1000, 1000, 1000]), 4)
        self.assertEqual(h_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)
        self.assertEqual(h_index([999] * 999), 999)
