import unittest
from lab4.task4.src.main import extract_brackets, find_errors


class TestCase(unittest.TestCase):

    def test_should_extract_brackets(self):
        # given
        s = 'foo(baa)[]{  {}'
        expected_result = [(3, '('), (7, ')'), (8, '['), (9, ']'), (10, '{'), (13, '{'), (14, '}')]

        # when
        res = extract_brackets(s)

        # then
        self.assertEqual(res, expected_result)

    def test_should_find_errors(self):
        # given
        s_1 = extract_brackets('foo(baa)[]{  {}')
        s_2 = extract_brackets('F(xxfd{dd}m[fh])()')
        expected_result = ['11', 'Success']

        # when
        res = [find_errors(s_1), find_errors(s_2)]

        # then
        self.assertEqual(res, expected_result)

    def test_task4(self):
        pass
