import unittest
import os
from lab4.task2.src.main import *
from lab4.utils import read_lines


current_path = os.path.abspath(os.path.dirname(__file__))
file_input = os.path.join(current_path, '../txtf/input.txt')
file_output = os.path.join(current_path, '../txtf/output.txt')
file_sample = os.path.join(current_path, '../txtf/sample.txt')
file_test = os.path.join(current_path, '../txtf/test.txt')


class Lab4Task2TestCase(unittest.TestCase):

    def test_should_queue(self):
        # given
        queue = Queue()
        expected_result = [1, 2, 3, 4]
        result = []

        # when
        queue.add(1)
        queue.add(2)
        result.append(queue.pop())
        queue.add(3)
        queue.add(4)
        for _ in range(3):
            result.append(queue.pop())

        # then
        self.assertEqual(result, expected_result)

    def test_should_run_commands(self):
        # given
        commands = read_lines(file_test, start=1)
        expected_result = [1, 2, 3, 4]

        # when
        result = run_commands(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_task2(self):
        # given
        commands = read_lines(file_test)
        expected_result = [1, 2, 3, 4]

        # when
        write_vars(file_input, *commands)
        task2()
        result = read_lines(file_output, data_type=int)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDown(cls):
        tmp = read_lines(file_sample)
        write_vars(file_input, *tmp)
