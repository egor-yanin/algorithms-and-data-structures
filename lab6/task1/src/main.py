from lab6.utils import read_lines, write_vars
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


def execute(commands: list[str]) -> list[str]:
    current_set = set()
    result = []
    for command in commands:
        char, x = command.split()
        x = int(x)
        if char == 'A':
            current_set.update([x])
        elif char == 'D':
            current_set.discard(x)
        elif char == '?':
            if x in current_set:
                result.append('Y')
            else:
                result.append('N')
    return result


def task1():
    command_list = read_lines(FILE_INPUT, start=1)
    ans = execute(command_list)
    write_vars(FILE_OUTPUT, *ans)


if __name__ == '__main__':
    task1()
