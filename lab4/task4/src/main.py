import os
from lab4.utils import read_lines, write_vars
from lab4.task5.src.main import Stack


OPENED_CLOSED = {'{': '}', '[': ']', '(': ')'}
current_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_dir, '../txtf/input.txt')
file_output = os.path.join(current_dir, '../txtf/output.txt')


def extract_brackets(s: str):
    return [(i, s[i]) for i in range(len(s)) if s[i] in '(){}[]']


def find_errors(sub: list[tuple[int, str]]):
    opened = Stack(len(sub))
    for num, symbol in sub:
        if symbol in '({[':
            opened.push((num, symbol))
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
