import unittest
import os
from lab4.task1.src.main import Stack, task1
from lab4.utils import read_lines, write_vars


current_path = os.path.abspath(os.path.dirname(__file__))
file_input = os.path.join(current_path, '../txtf/input.txt')
file_output = os.path.join(current_path, '../txtf/output.txt')
file_sample = os.path.join(current_path, '../txtf/sample.txt')
file_test = os.path.join(current_path, '../txtf/test.txt')


class Lab4Task1TestCase(unittest.TestCase):

    def test_should_push_stack(self):
        # given
        stack = Stack()
        expected_result = [1, 2, 3, 4]

        # when
        for i in range(1, 5):
            stack.push(i)
        result = stack.stack

        # then
        self.assertEqual(result, expected_result)

    def test_should_pop_stack(self):
        # given
        stack = Stack()
        expected_result = 4

        # when
        for i in range(1, 5):
            stack.push(i)
        result = stack.pop()

        # then
        self.assertEqual(result, expected_result)

    def test_task1(self):
        # given
        commands = read_lines(file_test)
        expected_result = [4, 3, 2]

        # when
        write_vars(file_input, *commands)
        task1()
        result = read_lines(file_output, data_type=int)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDown(cls):
        tmp = read_lines(file_sample)
        write_vars(file_input, *tmp)
