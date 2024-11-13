from lab3.utils import read_array, write_vars, print_time_memory, read_str_lines
import os


current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_script_dir, '../textsf/input.txt')
file_output = os.path.join(current_script_dir, '../textsf/output.txt')


@print_time_memory
def radix_sort(lst, phase):
    pattern = list(range(len(lst[0])))
    bins = [[] for _ in range(26)]
    for i in range(phase):
        a = [lst[-i-1][j] for j in pattern]
        word = enumerate([ord(c) - 97 for c in a])
        for j, c in word:
            bins[c].append(j)
        new_pattern = [x for q in bins for x in q]
        pattern = [pattern[j] for j in new_pattern]
        bins = [[] for _ in range(26)]
    pattern = [x + 1 for x in pattern]
    return pattern


def task7():
    n, m, k = read_array(file_input, with_len=False)[0]
    lst = read_str_lines(file_input, start=1, num=n)
    write_vars(file_output, radix_sort(lst, k))


if __name__ == '__main__':
    task7()
