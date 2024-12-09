import os
from lab4.utils import read_lines, write_vars, print_time_memory


class Stack:

    def __init__(self, size=10**6):
        self.stack = []
        self.size = size
        self.is_empty = True

    def push(self, x):
        if len(self.stack) >= self.size:
            raise IndexError
        self.stack.append(x)
        if self.is_empty:
            self.is_empty = False

    def pop(self):
        if self.is_empty:
            raise IndexError
        x = self.stack.pop()
        return x


def run_commands(command_list: list[str]):
    tmp = Stack()
    result = []
    for command in command_list:
        if command[0] == '+':
            num = int(command.split()[1])
            tmp.push(num)
        elif command[0] == '-':
            result.append(tmp.pop())
    return result


current_path = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_path, '../txtf/input.txt')
file_output = os.path.join(current_path, '../txtf/output.txt')


@print_time_memory
def task1():
    lst = read_lines(file_input, start=1)
    ans = run_commands(lst)
    write_vars(file_output, *ans)


if __name__ == '__main__':
    task1()
