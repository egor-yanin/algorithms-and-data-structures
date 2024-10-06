import time


def applying(n1, n2):
    result = [0] * (len(n1) + 1)
    n1 = n1[::-1]
    n2 = n2[::-1]
    for i in range(len(n1)):
        isum = n1[i] + n2[i] + result[i]
        if isum == 0:
            result[i] = 0
        elif isum == 1:
            result[i] = 1
        elif isum == 2:
            result[i] = 0
            result[i + 1] = 1
        elif isum == 3:
            result[i] = 1
            result[i + 1] = 1
    return result[::-1]


start = time.perf_counter()
with open('../tests/input.txt') as fin, open('../tests/output.txt', 'w') as fout:
    a, b = fin.readline().split()
    lst1 = [int(x) for x in a]
    lst2 = [int(x) for x in b]
    ans = applying(lst1, lst2)
    print('Затрачено времени: ', time.perf_counter() - start, 'сек.')
    fout.write(''.join([str(x) for x in ans]))
