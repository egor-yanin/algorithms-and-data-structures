import unittest
import os
from lab4.utils import write_vars, read_lines
from lab4.task12.src.main import Recruit, execute, task12


current_path = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_path, '../txtf/input.txt')
file_output = os.path.join(current_path, '../txtf/output.txt')


class Lab4Task12TestCase(unittest.TestCase):

    def test_should_stand(self):
        # given
        recruit = Recruit()
        expected_result = [2, 1, 3]

        # when
        recruit.stand_left(2, 1)
        recruit.stand_right(3, 1)

        # then
        self.assertEqual(recruit.formation, expected_result)

    def test_should_leave(self):
        # given
        recruit = Recruit()
        recruit.stand_right(2, 1)
        recruit.stand_right(3, 2)
        expected_result = [1, 3]

        # when
        recruit.leave(2)

        # then
        self.assertEqual(recruit.formation, expected_result)

    def test_should_name(self):
        # given
        recruit = Recruit()
        recruit.stand_right(2, 1)
        recruit.stand_right(3, 2)
        expected_result = (1, 3)

        # when
        result = recruit.name(2)

        # then
        self.assertEqual(result, expected_result)

    def test_should_execute(self):
        # given
        command_list = ['left 2 1', 'right 3 1', 'name 1']
        expected_result = ['2 3']

        # when
        result = execute(command_list)

        # then
        self.assertEqual(result, expected_result)

    def test_task12(self):
        # given
        file_test = os.path.join(current_path, '../txtf/test.txt')
        write_vars(file_input, *read_lines(file_test))
        expected_result = ['0 3']

        # when
        task12()
        result = read_lines(file_output)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        file_sample = os.path.join(current_path, '../txtf/sample.txt')
        write_vars(file_input, *read_lines(file_sample))
