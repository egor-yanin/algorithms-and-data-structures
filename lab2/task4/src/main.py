from math import floor
from utils import read_n_array, write_vars


def binary_search(lst, low, high, key):
    if high < low:
        return low - 1
    if low == high:
        return -1
    mid = low + floor((high - low) / 2)
    if key == lst[mid]:
        return mid
    elif key < lst[mid]:
        return binary_search(lst, low, mid - 1, key)
    else:
        return binary_search(lst, mid + 1, high, key)


def main(file='input.txt'):
    input_data = read_n_array(file, num=2)
    a, b = input_data[0][0], input_data[1][0]
    ans = []
    for i in b:
        ans.append(binary_search(a, 0, len(a), i))
    write_vars('../tests/output.txt', ans)
