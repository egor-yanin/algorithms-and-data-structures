from math import floor


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -10**9
    s = 0
    for i in range(mid, low - 1, -1):
        s += A[i]
        if s > left_sum:
            left_sum = s
            left_max = i
    right_sum = - 10**9
    s = 0
    for j in range(mid + 1, high + 1):
        s += A[j]
        if s > right_sum:
            right_sum = s
            right_max = j
    return left_max, right_max, left_sum + right_sum


def find_max_subarray(A, low, high):
    if low == high:
        return low, high, A[low]
    else:
        mid = floor((low + high) / 2)
        left_low, left_high, left_sum = find_max_subarray(A, low, mid)
        right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def main(file):
    with open(file) as fin, open('../tests/output.txt', 'w', encoding='UTF-16') as fout:
        headers = [x for x in fin.readline().split()]
        lst, date = [], []
        name = str()
        for s in fin.readlines():
            data = list(s.split())
            lst.append(float(data[4]))
            date.append(data[2])
            name = data[0]
        delta = [lst[i] - lst[i-1] for i in range(1, len(lst))]
        start, end, stonks = find_max_subarray(delta, 0, len(delta)-1)
        fout.write(f'''{name}
02.09.24 - 01.10.24
Дата покупки: {date[start][:2]}.{date[start][2:4]}.{date[start][4:]}
Дата продажи: {date[end][:2]}.{date[end][2:4]}.{date[end][4:]}
Прибыль: {stonks}''')
