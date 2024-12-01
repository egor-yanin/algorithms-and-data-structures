import unittest
import os
from lab4.task12.src.main import Recruit


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
        pass

    def test_should_name(self):
        pass

    def test_task12(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
