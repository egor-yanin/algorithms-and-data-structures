from lab3.utils import read_array, write_vars, print_time_memory
import os


current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../txtf/input.txt')
file_output = os.path.join(current_script_dir, '../txtf/output.txt')


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
    arr = read_array(file_input, with_len=False)[0]
    write_vars(file_output, h_index(arr))


if __name__ == '__main__':
    task5()
