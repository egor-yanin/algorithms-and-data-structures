import time
import tracemalloc


def read_array(file, start=0, num=1, with_len=True) -> list:
    res = []
    with open(file) as fin:
        lines = fin.readlines()[start:]
        if with_len:
            for s in range(0, num * 2, 2):
                ln = int(lines[s])
                lst = [int(x) for x in lines[s + 1].split()]
                res.append([lst, ln])
        else:
            for s in range(num):
                lst = [int(x) for x in lines[s].split()]
                res.append(lst)
    return res


def read_int(file, line=0) -> int:
    with open(file) as fin:
        return int(fin.readlines()[line])


def write_vars(file, *args, mode='w'):
    with open(file, mode) as fout:
        for i in args:
            if type(i) is list or type(i) is tuple:
                fout.write(' '.join([str(x) for x in i]) + '\n')
            else:
                fout.write(f'{i}\n')


def print_time_memory(task_func):
    def wrapper(*args, **kwargs):

        tracemalloc.start()
        start_time = time.time()

        result = task_func(*args, *kwargs)

        print("memory usage: ", tracemalloc.get_traced_memory()[1], " bytes")
        print("--- %s seconds ---" % (time.time() - start_time))
        print("\n")
        tracemalloc.stop()

        return result
    return wrapper


def is_sorted(lst, reverse=False):
    if reverse:
        return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
