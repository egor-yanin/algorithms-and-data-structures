from lab6.utils import read_lines, write_vars, print_time_memory
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')
fibonacci_list = [1, 1]


def extend_fib(lst: list, key):
    while lst[-1] < key:
        lst.append(lst[-1] + lst[-2])


def is_fibonacci(key):
    if fibonacci_list[-1] < key:
        extend_fib(fibonacci_list, key)
    return key in fibonacci_list


@print_time_memory
def task6():
    numbers = read_lines(FILE_INPUT, start=1, data_type=int)
    ans = []
    for num in numbers:
        if is_fibonacci(num):
            ans.append('Yes')
        else:
            ans.append('No')
    write_vars(FILE_OUTPUT, *ans)


if __name__ == '__main__':
    task6()
