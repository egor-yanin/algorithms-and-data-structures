from math import floor
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


def find_max_crossing_subarray(lst, low, mid, high):
    left_sum = -10**9
    s = 0
    for i in range(mid, low - 1, -1):
        s += lst[i]
        if s > left_sum:
            left_sum = s
            left_max = i
    right_sum = - 10**9
    s = 0
    for j in range(mid + 1, high + 1):
        s += lst[j]
        if s > right_sum:
            right_sum = s
            right_max = j
    return left_max, right_max, left_sum + right_sum


def find_max_subarray(lst, low=0, high=-10):
    if high == -10:
        high = len(lst) - 1
    if low == high:
        return low, high, lst[low]
    else:
        mid = floor((low + high) / 2)
        left_low, left_high, left_sum = find_max_subarray(lst, low, mid)
        right_low, right_high, right_sum = find_max_subarray(lst, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(lst, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def task6():
    with open(FILE_INPUT) as fin, open(FILE_OUTPUT, 'w', encoding='windows-1251') as fout:
        lst, date = [], []
        name = str()
        for s in fin.readlines():
            data = list(s.split())
            lst.append(float(data[4]))
            date.append(data[2])
            name = data[0]
        delta = [lst[i] - lst[i-1] for i in range(1, len(lst))]
        start, end, stonks = find_max_subarray(delta)
        fout.write(f'''{name}
02.09.24 - 01.10.24
Дата покупки: {date[start][:2]}.{date[start][2:4]}.{date[start][4:]}
Дата продажи: {date[end][:2]}.{date[end][2:4]}.{date[end][4:]}
Прибыль: {stonks}''')


if __name__ == '__main__':
    task6()
