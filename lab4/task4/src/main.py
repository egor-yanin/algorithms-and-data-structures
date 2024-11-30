from typing import Any
import os
from lab4.utils import read_lines, write_vars


OPENED_CLOSED = {'{': '}', '[': ']', '(': ')'}
current_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_dir, '../txtf/input.txt')
file_output = os.path.join(current_dir, '../txtf/output.txt')


class Stack:

    def __init__(self, size=10**6):
        self.stack = [Any] * size
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def add(self, x):
        if self.length < len(self.stack):
            self.stack[self.length] = x
            self.length += 1
        else:
            raise IndexError

    def seek_tail(self):
        return self.stack[self.length - 1]

    def remove(self):
        self.length -= 1

    def pop(self):
        if not self.is_empty():
            res = self.seek_tail()
            self.remove()
            return res
        else:
            raise IndexError


def extract_brackets(s: str):
    return [(i, s[i]) for i in range(len(s)) if s[i] in '(){}[]']


def find_errors(sub: list[tuple[int, str]]):
    opened = Stack(len(sub))
    for num, symbol in sub:
        if symbol in '({[':
            opened.add((num, symbol))
        else:
            if not opened.is_empty():
                char = opened.seek_tail()[1]
                if OPENED_CLOSED[char] == symbol:
                    opened.remove()
                else:
                    return str(num + 1)
            else:
                return str(num + 1)
    if opened.length != 0:
        num = opened.pop()[0]
        while opened.length != 0:
            num = opened.pop()[0]
        return str(num + 1)
    else:
        return 'Success'


def task4():
    line = read_lines(file_input, num=1)[0]
    res = find_errors(extract_brackets(line))
    write_vars(file_output, res)
