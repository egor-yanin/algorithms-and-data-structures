from lab7.utils import read_array, write_vars, print_time_memory
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


@print_time_memory
def common_subsequence_len(a, b, c):
    n1, n2, n3 = len(a), len(b), len(c)
    subseq_len = [[[0] * (n3 + 1) for _ in range(n2 + 1)] for __ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            for k in range(1, n3 + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    subseq_len[i][j][k] = subseq_len[i - 1][j - 1][k - 1] + 1
                else:
                    subseq_len[i][j][k] = max(subseq_len[i - 1][j][k], subseq_len[i][j - 1][k], subseq_len[i][j][k - 1])

    return subseq_len[n1][n2][n3]


def task5():
    a = read_array(FILE_INPUT, line=1)
    b = read_array(FILE_INPUT, line=3)
    c = read_array(FILE_INPUT, line=5)
    result = common_subsequence_len(a, b, c)
    write_vars(FILE_OUTPUT, result)


if __name__ == '__main__':
    task5()
