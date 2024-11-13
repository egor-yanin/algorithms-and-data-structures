from lab3.utils import is_sorted, read_array, write_vars, print_time_memory
import os


current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../textsf/input.txt')
file_output = os.path.join(current_script_dir, '../textsf/output.txt')


@print_time_memory
def pugalo_sort(lst, k):
    for i in range(len(lst) - k):
        if lst[i] > lst[i + k]:
            lst[i], lst[i + k] = lst[i + k], lst[i]


def task3():
    data = read_array(file_input, num=2, with_len=False)
    n, k = data[0]
    a = data[1]
    pugalo_sort(a, k)
    if is_sorted(a):
        write_vars(file_output, 'YES')
    else:
        write_vars(file_output, 'NO')


if __name__ == '__main__':
    task3()
