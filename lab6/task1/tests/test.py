import unittest
from lab6.task1.src.main import execute


class Lab6Task1TestCase(unittest.TestCase):

    def test_should_execute(self):
        # given
        command_list = ['A 2', 'A 2', 'A 3', 'D 2', 'D 4', '? 2', '? 3', '? 4']
        expected_result = ['N', 'Y', 'N']

        # when
        result = execute(command_list)

        # then
        self.assertEqual(result, expected_result)
