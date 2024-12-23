from lab6.utils import read_lines, write_vars, print_time_memory
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


def count_votes(data: list[str]) -> dict[str, int]:
    candidates = {}
    for line in data:
        name, votes = line.split()
        votes = int(votes)
        candidates[name] = candidates.get(name, 0) + votes
    return candidates


def stringify_votes(candidates: dict):
    return sorted(f'{name} {votes}' for name, votes in candidates.items())


@print_time_memory
def task5():
    data = read_lines(FILE_INPUT)
    write_vars(FILE_OUTPUT, *stringify_votes(count_votes(data)))


if __name__ == '__main__':
    task5()
