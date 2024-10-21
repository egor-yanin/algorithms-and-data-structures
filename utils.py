def read_n_array(file, start=0, num=1) -> list:
    res = []
    with open(file) as fin:
        lines = fin.readlines()[start:]
        for s in range(0, num * 2, 2):
            ln = int(lines[s])
            lst = [int(x) for x in lines[s+1].split()]
            res.append([lst, ln])
    return res


def read_array(file, start=0, num=1) -> list:
    res = []
    with open(file) as fin:
        lines = fin.readlines()[start:]
        for s in range(num):
            lst = [int(x) for x in lines[s].split()]
            res.append(lst)
    return res


def read_int(file, line=0) -> int:
    with open(file) as fin:
        return int(fin.readlines()[line])


def write_vars(file, *args, end=True):
    if end:
        with open(file, 'w') as fout:
            for i in args:
                if type(i) is list or type(i) is tuple:
                    fout.write(' '.join([str(x) for x in i]) + '\n')
                else:
                    fout.write(f'{i}\n')
    else:
        with open(file, 'a') as fout:
            for i in args:
                if type(i) is list or type(i) is tuple:
                    fout.write(' '.join([str(x) for x in i]) + '\n')
                else:
                    fout.write(f'{i}\n')
