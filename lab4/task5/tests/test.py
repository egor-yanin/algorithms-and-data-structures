import os
import unittest
from lab4.task5.src.main import Stack


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

