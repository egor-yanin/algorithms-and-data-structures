import time
import psutil


def insertion(lst):
    for j in range(1, len(lst)):
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > key:
            lst[i + 1] = lst[i]
            i = i - 1
        lst[i + 1] = key
    return lst


start = time.perf_counter()
with open('../tests/input.txt') as fin, open('../tests/output.txt', 'w') as fout:
    n = int(fin.readline())
    A = [int(x) for x in fin.readline().split()]
    print('Затрачено времени: ', time.perf_counter() - start, 'сек.')
    print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
    fout.write(' '.join([str(x) for x in insertion(A)]))