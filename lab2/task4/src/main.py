from math import floor


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
    with open(file) as fin, open('output.txt', 'w') as fout:
        n = int(fin.readline())
        a = [int(x) for x in fin.readline().split()]
        k = int(fin.readline())
        b = [int(x) for x in fin.readline().split()]
        ans = []
        for i in b:
            ans.append(binary_search(a, 0, len(a), i))
        print(*ans, sep=' ', file=fout)
