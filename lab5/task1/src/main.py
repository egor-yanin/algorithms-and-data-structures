import os
from lab5.utils import read_lines, write_vars, print_time_memory


current_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_dir, '../txtf/input.txt')
file_output = os.path.join(current_dir, '../txtf/output.txt')


def is_correct_node(heap, index):
    parent = index // 2
    left = index * 2
    right = index * 2 + 1
    flag = True
    if heap[parent] > heap[index]:
        flag = False
    if left < len(heap) and heap[left] < heap[index]:
        flag = False
    if right < len(heap) and heap[right] < heap[index]:
        flag = False
    return flag


def is_heap(lst):
    heap = [0] + lst
    flag = True
    for i in range(2, len(heap)):
        if not is_correct_node(heap, i):
            flag = False
    return flag


@print_time_memory
def task1():
    lst = read_lines(file_input, start=1, data_type=int)
    if is_heap(lst):
        write_vars(file_output, 'YES')
    else:
        write_vars(file_output, 'NO')


if __name__ == '__main__':
    task1()
