from lab7.utils import read_array, write_vars, print_time_memory
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


@print_time_memory
def longest_increasing_subsequence(seq):
    n = len(seq)
    if n == 0:
        return []
    max_sub_len = [1] * n
    prev = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j] and max_sub_len[i] < max_sub_len[j] + 1:
                max_sub_len[i] = max_sub_len[j] + 1
                prev[i] = j
    max_index = max_sub_len.index(max(max_sub_len))
    subsequence = []
    while max_index != -1:
        subsequence.append(seq[max_index])
        max_index = prev[max_index]
    return subsequence[::-1]


def task6():
    seq = read_array(FILE_INPUT, line=1)
    result = longest_increasing_subsequence(seq)
    write_vars(FILE_OUTPUT, len(result), result)


if __name__ == '__main__':
    task6()
