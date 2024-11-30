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