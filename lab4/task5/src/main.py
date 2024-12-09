from typing import Any
from lab4.utils import read_lines, write_vars, print_time_memory
import os


current_path = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_path, '../txtf/input.txt')
file_output = os.path.join(current_path, '../txtf/output.txt')


class Stack:

    def __init__(self, size=10**6):
        self.stack = [Any] * size
        self.max_stack = []
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        if self.length < len(self.stack):
            self.stack[self.length] = x
            if self.max_stack == [] or x > self.max_stack[-1][0]:
                self.max_stack.append((x, self.length))
            self.length += 1
        else:
            raise IndexError

    def seek_tail(self):
        return self.stack[self.length - 1]

    def remove(self):
        if self.length - 1 == self.max_stack[-1][1]:
            self.max_stack.pop()
        self.length -= 1

    def pop(self):
        if not self.is_empty():
            res = self.seek_tail()
            self.remove()
            return res
        else:
            raise IndexError

    def seek_max(self):
        return self.max_stack[-1][0]


def execute(commands: list[str]):
    st = Stack()
    res = []
    for com in commands:
        if com[:4] == 'push':
            st.push(int(com.split()[1]))
        elif com[:3] == 'pop':
            st.pop()
        elif com[:3] == 'max':
            res.append(st.seek_max())
        else:
            raise ValueError
    return res


@print_time_memory
def task5():
    com_list = read_lines(file_input, start=1)
    ans = execute(com_list)
    write_vars(file_output, *ans)


if __name__ == '__main__':
    task5()
