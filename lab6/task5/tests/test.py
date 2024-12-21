from lab6.utils import write_vars, read_lines
from lab6.task2.src.main import execute
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab6Task2TestCase(unittest.TestCase):


    @classmethod
    def tearDownClass(cls):
        write_vars(FILE_INPUT, *read_lines(FILE_SAMPLE))
