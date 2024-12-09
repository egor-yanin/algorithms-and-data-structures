import os
from lab4.utils import read_lines, write_vars, print_time_memory


class Queue:

    def __init__(self, size=10**6):
        self.queue = [0] * size
        self.head = 0
        self.tail = 0
        self.is_empty = True
        self.is_full = False

    def add(self, x):
        if self.is_full:
            raise IndexError
        self.queue[self.tail] = x
        if self.tail == len(self.queue):
            self.tail = 0
        else:
            self.tail += 1
        if self.is_empty:
            self.is_empty = False
        if self.tail == self.head:
            self.is_full = True

    def pop(self):
        if self.is_empty:
            raise IndexError
        x = self.queue[self.head]
        if self.head == len(self.queue):
            self.head = 0
        else:
            self.head += 1
        if self.tail == self.head:
            self.is_empty = True
        return x

    def seek_head(self):
        return self.queue[self.head]

    def seek_tail(self):
        return self.queue[self.tail]


def run_commands(command_list: list[str]):
    tmp = Queue()
    result = []
    for command in command_list:
        if command[0] == '+':
            num = int(command.split()[1])
            tmp.add(num)
        elif command[0] == '-':
            result.append(tmp.pop())
    return result


current_path = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_path, '../txtf/input.txt')
file_output = os.path.join(current_path, '../txtf/output.txt')


@print_time_memory
def task2():
    lst = read_lines(file_input, start=1)
    ans = run_commands(lst)
    write_vars(file_output, *ans)


if __name__ == '__main__':
    task2()
