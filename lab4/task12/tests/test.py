import unittest
import os
from lab4.task12.src.main import Recruit, execute


class TestCase(unittest.TestCase):

    def test_should_stand(self):
        # given
        tmp = Recruit()
        expected_result = [2, 1, 3]

        # when
        tmp.stand_left(2, 1)
        tmp.stand_right(3, 1)

        # then
        self.assertEqual(tmp.formation, expected_result)

    def test_should_leave(self):
        # given
        tmp = Recruit()
        tmp.stand_right(2, 1)
        tmp.stand_right(3, 2)
        expected_result = [1, 3]

        # when
        tmp.leave(2)

        # then
        self.assertEqual(tmp.formation, expected_result)

    def test_should_name(self):
        # given
        tmp = Recruit()
        tmp.stand_right(2, 1)
        tmp.stand_right(3, 2)
        expected_result = (1, 3)

        # when
        res = tmp.name(2)

        # then
        self.assertEqual(res, expected_result)

    def test_should_execute(self):
        command_list = ['left 2 1', 'right 3 1', 'name 1']
        expected_result = ['2 3']

        res = execute(command_list)

        self.assertEqual(res, expected_result)
        pass

    def test_task12(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
