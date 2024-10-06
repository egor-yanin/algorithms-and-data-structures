import time


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1, i, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst


start = time.perf_counter()
with open('../tests/input.txt') as fin, open('../tests/output.txt', 'w') as fout:
    n = int(fin.readline())
    A = [int(x) for x in fin.readline().split()]
    sorted_A = bubble_sort(A)
    print('Затрачено времени: ', time.perf_counter() - start, 'сек.')
    fout.write(' '.join([str(x) for x in sorted_A]))
    flag = True
    for i in range(len(sorted_A) - 1):
        if sorted_A[i] > sorted_A[i + 1]:
            flag = False
    if flag:
        print('Список отсортирован')
    else:
        print('Список не отсортирован')
