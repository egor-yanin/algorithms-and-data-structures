import os
from lab5.utils import write_vars, read_lines, read_array


current_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_dir, '../txtf/input.txt')
file_output = os.path.join(current_dir, '../txtf/output.txt')


class LowerHeap:
    def __init__(self, lst: list[int]):
        self.heap_list = [None] + lst.copy()
        self.heap_size = len(lst)
        self.swaps = []
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

    def get_swaps(self):
        return self.swaps

    def swap(self, i, j):
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]
        self.swaps.append((i - 1, j - 1))

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


def task4():
    lst = read_array(file_input, line=1)
    heap = LowerHeap(lst)
    swaps = heap.get_swaps()
    write_vars(file_output, len(swaps), *swaps)


if __name__ == '__main__':
    task4()
