from lab2.task4.src.main import binary_search, task2
from lab2.utils import write_vars, read_array
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')
FILE_TEST = os.path.join(CURRENT_DIR, '../txtf/test.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab2Task4TestCase(unittest.TestCase):
    def test_should_binary_search(self):
        # given
        lst = [0, 3, 4, 6, 8]
        expected_result = 3

        # when
        result = binary_search(lst, 6)

        # then
        self.assertEqual(result, expected_result)

    def test_should_task2(self):
        # given
        data = read_array(FILE_TEST, num=2)
        write_vars(FILE_INPUT, data[0][1], data[0][0], data[1][1], data[1][0])
        expected_result = [3, 1, -1]

        # when
        task2()
        result = read_array(FILE_OUTPUT, with_len=False)[0]

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        data = read_array(FILE_SAMPLE, num=2)
        write_vars(FILE_INPUT, data[0][1], data[0][0], data[1][1], data[1][0])
        pass
