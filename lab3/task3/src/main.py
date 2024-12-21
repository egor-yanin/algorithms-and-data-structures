from lab3.utils import is_sorted, read_array, write_vars, print_time_memory
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


@print_time_memory
def pugalo_sort(lst, k):
    for i in range(len(lst) - k):
        if lst[i] > lst[i + k]:
            lst[i], lst[i + k] = lst[i + k], lst[i]


def task3():
    data = read_array(FILE_INPUT, num=2, with_len=False)
    n, k = data[0]
    lst = data[1]
    pugalo_sort(lst, k)
    if is_sorted(lst):
        write_vars(FILE_OUTPUT, 'YES')
    else:
        write_vars(FILE_OUTPUT, 'NO')


if __name__ == '__main__':
    task3()
