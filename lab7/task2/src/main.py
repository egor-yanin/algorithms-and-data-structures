from lab7.utils import read_lines, write_vars, print_time_memory
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


@print_time_memory
def calculate(n: int):
    path_len = [0] * (n + 1)
    prev = [0] * (n + 1)
    for i in range(2, n + 1):
        path_len[i] = 1 + path_len[i - 1]
        prev[i] = i - 1
        if i % 2 == 0 and path_len[i // 2] + 1 < path_len[i]:
            path_len[i] = path_len[i // 2] + 1
            prev[i] = i // 2
        if i % 3 == 0 and path_len[i // 3] + 1 < path_len[i]:
            path_len[i] = path_len[i // 3] + 1
            prev[i] = i // 3
    seq = []
    while n != 0:
        seq.append(n)
        n = prev[n]
    return seq[::-1]


def task2():
    number = read_lines(FILE_INPUT, num=1, data_type=int)[0]
    result = calculate(number)
    write_vars(FILE_OUTPUT, len(result) - 1, result)


if __name__ == '__main__':
    task2()
