from lab3.utils import is_sorted, read_array, write_vars, print_time_memory


@print_time_memory
def pugalo_sort(lst, k):
    for i in range(len(lst) - k):
        if lst[i] > lst[i + k]:
            lst[i], lst[i + k] = lst[i + k], lst[i]


def main():
    data = read_array('../xtxt/input.txt', num=2, with_len=False)
    n, k = data[0]
    a = data[1]
    pugalo_sort(a, k)
    if is_sorted(a):
        write_vars('../xtxt/output.txt', 'YES')
    else:
        write_vars('../xtxt/output.txt', 'NO')


if __name__ == '__main__':
    main()
