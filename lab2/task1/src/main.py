from math import floor
from lab2.utils import read_array, write_vars


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


def merge_sort(lst, p, r):
    if p < r:
        q = floor((p + r) / 2)
        lst = merge_sort(lst, p, q)
        lst = merge_sort(lst, q + 1, r)
        lst = merge(lst, p, q, r)
        return lst
    else:
        return lst


def main(file):
    m, n = read_array(file, with_len=True)[0]
    write_vars('../tests/output.txt', merge_sort(m, 0, n - 1))
