from math import floor
from lab2.utils import read_array, write_vars
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


def binary_search(lst, key, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    if high < low:
        return low - 1
    mid = low + floor((high - low) / 2)
    if key == lst[mid]:
        return mid
    if high == mid == low:
        return -1
    elif key < lst[mid]:
        return binary_search(lst, key, low, mid - 1)
    else:
        return binary_search(lst, key, mid + 1, high)


def task2():
    input_data = read_array(FILE_INPUT, num=2, with_len=True)
    lst, search_list = input_data[0][0], input_data[1][0]
    ans = []
    for i in search_list:
        ans.append(binary_search(lst, i))
    write_vars(FILE_OUTPUT, ans)


if __name__ == '__main__':
    task2()
