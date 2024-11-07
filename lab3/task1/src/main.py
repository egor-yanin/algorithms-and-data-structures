from lab3.utils import read_array, write_vars
import random


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


def quick_sort(lst, start, end):
    if start < end:
        q = partition(lst, start, end)
        quick_sort(lst, start, q - 1)
        quick_sort(lst, q + 1, end)


def randomized_partition(lst, start, end):
    i = random.randint(start, end)
    lst[start], lst[i] = lst[i], lst[start]
    return partition(lst, start, end)


def randomized_quick_sort(lst, start, end):
    if start < end:
        q = randomized_partition(lst, start, end)
        randomized_quick_sort(lst, start, q - 1)
        randomized_quick_sort(lst, q + 1, end)


if __name__ == '__main__':
    a = read_array('input.txt')[0][0]
    quick_sort(a, 0, len(a) - 1)
    write_vars('output.txt', a)

