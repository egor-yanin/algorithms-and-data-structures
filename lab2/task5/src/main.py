from lab2.utils import read_array, write_vars, print_time_memory
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


def majority(lst):
    n = len(lst)
    mid = n // 2
    if n == 1:
        return lst[0], 1
    left_list = lst[:mid]
    right_list = lst[mid:]
    left_m = majority(left_list)
    left_count = right_list.count(left_m[0])
    right_m = majority(right_list)
    right_count = left_list.count(right_m[0])
    if left_count + left_m[1] > n // 2:
        return left_m[0], left_m[1] + left_count
    if right_count + right_m[1] > n // 2:
        return right_m[0], right_m[1] + right_count
    return None, 0


def task5():
    lst = read_array(FILE_INPUT, with_len=True)[0][0]
    m = majority(lst)
    if m[0] is None:
        write_vars(FILE_OUTPUT, '0')
    else:
        write_vars(FILE_OUTPUT, '1')
