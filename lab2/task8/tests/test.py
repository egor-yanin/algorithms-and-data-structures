from lab2.task8.src.main import addition, multiply
from lab2.utils import read_lines, write_vars
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FIlE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab2Task8TestCase(unittest.TestCase):
    def test_should_addition(self):
        # given
        polynom_a, polynom_b = (1, 2, 3, 0), (2, 4, 5)
        expected_result = (1, 4, 7, 5)

        # when
        result = addition(polynom_a, polynom_b)

        # then
        self.assertEqual(result, expected_result)

    def test_should_multiply(self):
        # given
        polynom_a, polynom_b = (1, 2, 3), (2, 4, 5)
        expected_result = (2, 8, 19, 22, 15)

        # when
        result = multiply(polynom_a, polynom_b)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(FILE_INPUT, *read_lines(FIlE_SAMPLE))
