import unittest
import os
from lab4.task4.src.main import extract_brackets, find_errors, task4
from lab4.utils import read_lines, write_vars


current_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_dir, '../txtf/input.txt')
file_output = os.path.join(current_dir, '../txtf/output.txt')
file_sample = os.path.join(current_dir, '../txtf/sample.txt')
file_test = os.path.join(current_dir, '../txtf/test.txt')


class Task4TestCase(unittest.TestCase):

    def test_should_extract_brackets(self):
        # given
        s = 'foo(baa)[]{  {}'
        expected_result = [(3, '('), (7, ')'), (8, '['), (9, ']'), (10, '{'), (13, '{'), (14, '}')]

        # when
        result = extract_brackets(s)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_errors(self):
        # given
        s_1 = extract_brackets('foo(baa)[]{  {}')
        s_2 = extract_brackets('F(xxfd{dd}m[fh])()')
        expected_result = ['11', 'Success']

        # when
        result = [find_errors(s_1), find_errors(s_2)]

        # then
        self.assertEqual(result, expected_result)

    def test_task4(self):
        # given
        s = read_lines(file_test)[0]
        write_vars(file_input, s)
        expected_result = '11'

        # when
        task4()
        result = read_lines(file_output)[0]

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        s = read_lines(file_sample)[0]
        write_vars(file_input, s)
