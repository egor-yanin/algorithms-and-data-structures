from math import floor
from lab2.utils import read_array, write_vars
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


def merge(lst, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [lst[p + i] for i in range(0, n1)]
    right = [lst[q + j + 1] for j in range(0, n2)]
    i, j = 0, 0
    for k in range(p, r + 1):
        if i == len(left):
            lst[k:r + 1] = right[j:len(right)]
            break
        elif j == len(right):
            lst[k:r + 1] = left[i:len(left)]
            break
        elif left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
    return lst


def merge_sort(lst, p=0, r=-1):
    if r == -1:
        r = len(lst) - 1
    if p < r:
        q = floor((p + r) / 2)
        lst = merge_sort(lst, p, q)
        lst = merge_sort(lst, q + 1, r)
        lst = merge(lst, p, q, r)
        return lst
    else:
        return lst


def task1():
    lst, n = read_array(FILE_INPUT, with_len=True)[0]
    write_vars(FILE_OUTPUT, merge_sort(lst))


if __name__ == '__main__':
    task1()
