from lab3.utils import read_array, write_vars, print_time_memory
import random
import sys
import os

sys.setrecursionlimit(10**6)
current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../txtf/input.txt')
file_output = os.path.join(current_script_dir, '../txtf/output.txt')


def partition(lst, start, end):
    x = lst[end]
    i = start - 1
    for j in range(start, end):
        if lst[j] <= x:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[end] = lst[end], lst[i + 1]
    return i + 1


def partition3(lst, start, end):
    x = lst[end]
    i = start - 1
    p = start - 1
    for j in range(start, end):
        if lst[j] < x:
            i += 1
            p += 1
            lst[i], lst[j] = lst[j], lst[i]
            lst[j], lst[p] = lst[p], lst[j]
        if lst[j] == x:
            p += 1
            lst[p], lst[j] = lst[j], lst[p]
    lst[p + 1], lst[end] = lst[end], lst[p + 1]
    return i + 1, p + 1


def quick_sort(lst, start=0, end=-1):
    if end == -1:
        end = len(lst) - 1
    if start < end:
        q = partition(lst, start, end)
        quick_sort(lst, start, q - 1)
        quick_sort(lst, q + 1, end)


def randomized_partition(lst, start, end, part3=False):
    i = random.randint(start, end)
    lst[start], lst[i] = lst[i], lst[start]
    if part3:
        return partition3(lst, start, end)
    else:
        return partition(lst, start, end)


def randomized_quick_sort(lst, start=0, end=-1, part3=False):
    if end == -1:
        end = len(lst) - 1
    if start < end:
        if part3:
            q, p = randomized_partition(lst, start, end, part3=True)
        else:
            q = randomized_partition(lst, start, end, part3=False)
            p = q
        randomized_quick_sort(lst, start, q - 1)
        randomized_quick_sort(lst, p + 1, end)


@print_time_memory
def task1():
    a = read_array(file_input)[0][0]
    randomized_quick_sort(a, 0, len(a) - 1)
    write_vars(file_output, a)


if __name__ == '__main__':
    task1()
