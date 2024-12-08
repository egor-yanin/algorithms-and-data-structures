import os
from lab5.utils import read_lines, write_vars
from lab5.task4.src.main import LowerHeap


current_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_dir, '../txtf/input.txt')
file_output = os.path.join(current_dir, '../txtf/output.txt')


class LowerPriorityQueue(LowerHeap):
    def __init__(self):
        super().__init__([])

    def heap_minimum(self) -> int:
        return self.heap_list[1]

    def extract_min(self):
        if self.heap_size == 0:
            return '*'
        maximum = self.heap_minimum()
        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_size -= 1
        if self.heap_size < 1:
            self.heap_list[0] = None
            return maximum
        self.max_heapify(1)
        return maximum

    def get_index(self, x):
        for i, key in enumerate(self.heap_list):
            if key == x:
                return i
        return -1

    def decrease_key(self, old_key, new_key):
        if new_key > self.heap_list[old_key]:
            raise ValueError
        self.heap_list[old_key] = new_key
        while old_key > 1 and self.heap_list[self.get_parent(old_key)] > self.heap_list[old_key]:
            self.swap(old_key, self.get_parent(old_key))
            old_key = self.get_parent(old_key)

    def insert(self, x):
        self.heap_size += 1
        self.heap_list.append(10**9)
        self.decrease_key(self.heap_size, x)


def execute(commands: list[str]) -> list:
    queue = LowerPriorityQueue()
    addition_list = [0] * len(commands)
    result = []
    for i in range(len(commands)):
        command = commands[i]
        if command.split()[0] == 'A':
            x = int(command.split()[1])
            queue.insert(x)
            addition_list[i] = x
        elif command.split()[0] == 'X':
            result.append(queue.extract_min())
        elif command.split()[0] == 'D':
            x, y = map(int, command.split()[1:])
            element = queue.get_index(addition_list[x - 1])
            queue.decrease_key(element, y)
            addition_list[x - 1] = y
    return result


def task6():
    command_list = read_lines(file_input, start=1)
    ans = execute(command_list)
    write_vars(file_output, *ans)


if __name__ == '__main__':
    task6()
