import os
import unittest
from lab4.task5.src.main import Stack, task5
from lab4.utils import read_lines, write_vars


current_path = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_path, '../txtf/input.txt')
file_output = os.path.join(current_path, '../txtf/output.txt')
file_sample = os.path.join(current_path, '../txtf/sample.txt')


class TestCase(unittest.TestCase):

    def test_should_push_pop(self):
        # given
        tmp = Stack()
        expected_result = [3, 2]
        res = []

        # when
        tmp.push(1)
        tmp.push(2)
        tmp.push(3)
        for _ in range(2):
            res.append(tmp.pop())

        # then
        self.assertEqual(res, expected_result)

    def test_should_seek_max(self):
        # given
        tmp = Stack()
        expected_result = 5

        # when
        tmp.push(5)
        tmp.push(1)
        tmp.push(-3)
        tmp.push(41)
        tmp.pop()
        res = tmp.seek_max()

        # then
        self.assertEqual(res, expected_result)

    def test_task5(self):
        # given
        file_test = os.path.join(current_path, '../txtf/test.txt')
        write_vars(file_input, *read_lines(file_test))
        expected_result = ['9', '9', '3']

        # when
        task5()
        res = read_lines(file_output)

        self.assertEqual(res, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(file_input, read_lines(file_sample))
