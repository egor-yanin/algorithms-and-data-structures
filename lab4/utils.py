import tracemalloc
import time


def read_lines(file, num=-1, start=0, data_type=str):
    with open(file) as f:
        if num == -1:
            return [data_type(x.strip()) for x in f.readlines()[start:]]
        else:
            return [data_type(x.strip()) for x in f.readlines()[start:start+num]]


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
