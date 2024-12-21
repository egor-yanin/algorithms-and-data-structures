from lab3.utils import read_array, write_vars, print_time_memory
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


@print_time_memory
def h_index(citations):
    h_arr = [0] * (max(citations) + 1)
    for i in citations:
        h_arr[i] += 1
    for i in range(len(h_arr) - 2, -1, -1):
        h_arr[i] += h_arr[i+1]
    h = -1
    for i, n in enumerate(h_arr):
        if i <= n:
            h += 1
        else:
            break
    return h


def task5():
    arr = read_array(FILE_INPUT, with_len=False)[0]
    write_vars(FILE_OUTPUT, h_index(arr))


if __name__ == '__main__':
    task5()
