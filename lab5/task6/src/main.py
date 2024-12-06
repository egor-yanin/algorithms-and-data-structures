import os
from lab5.utils import print_time_memory, read_lines, write_vars


current_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_dir, '../txtf/input.txt')
file_output = os.path.join(current_dir, '../txtf/output.txt')


class LowerHeap:
    def __init__(self, lst: list[int]):
        self.heap_list = [None] + lst.copy()
        self.heap_size = len(lst)
        for i in range(self.heap_size // 2, 0, -1):
            self.max_heapify(i)

    def get_node_data(self, i: int):
        return self.heap_list[i]

    def get_list(self):
        return self.heap_list[1:]

    @staticmethod
    def get_left(i: int):
        return 2 * i

    @staticmethod
    def get_right(i: int):
        return 2 * i + 1

    @staticmethod
    def get_parent(i: int):
        return i // 2

    def swap(self, i, j):
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]

    def max_heapify(self, i: int):
        left = self.get_left(i)
        right = self.get_right(i)
        if left <= self.heap_size and self.get_node_data(left) < self.get_node_data(i):
            smallest = left
        else:
            smallest = i
        if right <= self.heap_size and self.get_node_data(right) < self.get_node_data(smallest):
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            self.max_heapify(smallest)


class LowerPriorityQueue(LowerHeap):
    def __init__(self):
        super().__init__([])

    def heap_minimum(self) -> int:
        return self.heap_list[1]

    def extract_min(self):
        if self.heap_minimum() is None:
            return '*'
        maximum = self.heap_minimum()
        self.heap_list[0] = self.heap_list[self.heap_size]
        self.heap_size -= 1
        if self.heap_size < 1:
            self.heap_list[0] = None
            return maximum
        self.max_heapify(0)
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
    result = []
    for command in commands:
        if command.split()[0] == 'A':
            x = int(command.split()[1])
            queue.insert(x)
        elif command.split()[0] == 'X':
            result.append(queue.extract_min())
        elif command.split()[0] == 'D':
            x, y = map(int, command.split()[1:])
            element = x
            queue.decrease_key(element, y)
    return result


def task6():
    command_list = read_lines(file_input, start=1)
    ans = execute(command_list)
    write_vars(file_output, *ans)
