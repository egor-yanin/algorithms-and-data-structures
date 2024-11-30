import unittest
import os
from lab4.task2.src.main import *
from lab4.utils import read_lines


current_path = os.path.abspath(os.path.dirname(__file__))
file_input = os.path.join(current_path, '../txtf/input.txt')
file_output = os.path.join(current_path, '../txtf/output.txt')
file_sample = os.path.join(current_path, '../txtf/sample.txt')
file_test = os.path.join(current_path, '../txtf/test.txt')


class TestCase(unittest.TestCase):

    def test_should_queue(self):
        # given
        q = Queue()
        expected_result = [1, 2, 3, 4]
        res = []

        # when
        q.add(1)
        q.add(2)
        res.append(q.pop())
        q.add(3)
        q.add(4)
        for _ in range(3):
            res.append(q.pop())

        # then
        self.assertEqual(res, expected_result)

    def test_should_run_commands(self):
        # given
        coms = read_lines(file_test, start=1)
        expected_result = [1, 2, 3, 4]

        # when
        res = run_commands(coms)

        # then
        self.assertEqual(res, expected_result)

    def test_task2(self):
        # given
        coms = read_lines(file_test)
        expected_result = [1, 2, 3, 4]

        # when
        write_vars(file_input, *coms)
        task2()
        res = read_lines(file_output, data_type=int)

        # then
        self.assertEqual(res, expected_result)

    @classmethod
    def tearDown(cls):
        tmp = read_lines(file_sample)
        write_vars(file_input, *tmp)
