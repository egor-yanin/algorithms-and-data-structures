from lab2.task5.src.main import majority
from lab2.utils import read_array, write_vars
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')
FILE_TEST_TRUE = os.path.join(CURRENT_DIR, '../txtf/true.txt')
FILE_TEST_FALSE = os.path.join(CURRENT_DIR, '../txtf/false.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab2Task5TestCase(unittest.TestCase):
    def test_should_majority_false(self):
        # given
        data = read_array(FILE_TEST_FALSE)[0][0]
        expected_result = None

        # when
        result = majority(data)[0]

        # then
        self.assertEqual(result, expected_result)

    def test_should_majority_true(self):
        # given
        data = read_array(FILE_TEST_TRUE)[0][0]
        expected_result = 2

        # when
        result = majority(data)[0]

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        data = read_array(FILE_SAMPLE)[0]
        write_vars(FILE_INPUT, data[1], data[0])
