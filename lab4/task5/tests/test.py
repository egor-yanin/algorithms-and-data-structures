import os
import unittest
from lab4.task5.src.main import Stack, task5
from lab4.utils import read_lines, write_vars


current_path = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_path, '../txtf/input.txt')
file_output = os.path.join(current_path, '../txtf/output.txt')
file_sample = os.path.join(current_path, '../txtf/sample.txt')


class Lab4Task5TestCase(unittest.TestCase):

    def test_should_push_pop(self):
        # given
        stack = Stack()
        expected_result = [3, 2]
        result = []

        # when
        stack.push(1)
        stack.push(2)
        stack.push(3)
        for _ in range(2):
            result.append(stack.pop())

        # then
        self.assertEqual(result, expected_result)

    def test_should_seek_max(self):
        # given
        stack = Stack()
        expected_result = 5

        # when
        stack.push(5)
        stack.push(1)
        stack.push(-3)
        stack.push(41)
        stack.pop()
        result = stack.seek_max()

        # then
        self.assertEqual(result, expected_result)

    def test_task5(self):
        # given
        file_test = os.path.join(current_path, '../txtf/test.txt')
        write_vars(file_input, *read_lines(file_test))
        expected_result = ['9', '9', '3']

        # when
        task5()
        result = read_lines(file_output)

        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(file_input, read_lines(file_sample))
