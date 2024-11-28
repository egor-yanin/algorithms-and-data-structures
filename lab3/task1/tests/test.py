from lab3.utils import read_array, is_sorted, write_vars
from lab3.task1.src.main import partition3, task1, quick_sort, randomized_quick_sort
import unittest
import os


current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../txtf/input.txt')
file_output = os.path.join(current_script_dir, '../txtf/output.txt')


class TestCase(unittest.TestCase):

    def test_should_partition3(self):
        expected_partition = [3, 5]
        expected_result = [1, 2, 1, 3, 3, 3, 5, 4]
        file = os.path.join(current_script_dir, '../txtf/partition3test.txt')

        a1 = read_array(file)[0][0]
        m1, m2 = partition3(a1, 0, len(a1) - 1)

        self.assertEqual([m1, m2], expected_partition)
        self.assertEqual(a1, expected_result)

    def test_should_randomized_quick_sort(self):
        files = ['worst_case.txt', 'average_case.txt', 'best_case.txt']
        paths = [os.path.join(current_script_dir, f'../txtf/{f}') for f in files]

        for f in paths:
            for a, n in read_array(f, num=2, with_len=True):
                write_vars(file_input, n, a)
                print('Файл', f)
                print('Массив размера', n)
                task1()
                a = read_array(file_output, with_len=False)

                self.assertTrue(is_sorted(a))

    def test_should_quick_sort(self):
        files = ['worst_case.txt', 'average_case.txt', 'best_case.txt']
        paths = [os.path.join(current_script_dir, f'../txtf/{f}') for f in files]

        for f in paths:
            for a, n in read_array(f, num=2, with_len=True):
                print()
                print('Файл', f)
                print('Массив размера', n)
                quick_sort(a, 0, len(a) - 1)

                self.assertTrue(is_sorted(a))

    @classmethod
    def tearDownClass(cls):
        file_sample = os.path.join(current_script_dir, '../txtf/sample.txt')
        data_sample = read_array(file_sample)
        write_vars(file_input, *data_sample[0][::-1])
