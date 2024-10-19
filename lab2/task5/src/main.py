def majority(lst):
    n = len(lst)
    mid = n // 2
    if n == 1:
        return lst[0], 1
    left_list = lst[:mid]
    right_list = lst[mid:]
    left_m = majority(left_list)
    left_count = right_list.count(left_m[0])
    right_m = majority(right_list)
    right_count = left_list.count(right_m[0])
    if left_count + left_m[1] > n // 2:
        return left_m[0], left_m[1] + left_count
    if right_count + right_m[1] > n // 2:
        return right_m[0], right_m[1] + right_count
    return None, 0


def main(file='input.txt'):
    with open(file) as fin, open('output.txt', 'w') as fout:
        N = int(fin.readline())
        A = [int(x) for x in fin.readline().split()]
        m = majority(A)
        if m[0] is None:
            fout.write('0')
        else:
            fout.write('1')