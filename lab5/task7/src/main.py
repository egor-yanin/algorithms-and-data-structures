from lab5.task6.src.main import LowerHeap
from lab5.utils import read_lines, write_vars, print_time_memory
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_dir, '../txtf/input.txt')
file_output = os.path.join(current_dir, '../txtf/output.txt')


@print_time_memory
def heap_sort(lst):
    heap = LowerHeap(lst)
    for i in range(len(lst), 1, -1):
        heap.swap(1, i)
        heap.heap_size -= 1
        heap.max_heapify(1)
    return heap.heap_list[1:]


def task7():
    lst = read_lines(file_input, start=1, data_type=int)
    write_vars(file_output, heap_sort(lst))


if __name__ == '__main__':
    task7()
