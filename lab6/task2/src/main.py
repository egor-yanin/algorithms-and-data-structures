from lab6.utils import print_time_memory, read_lines, write_vars
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


@print_time_memory
def execute(commands: list[str]) -> list[str]:
    reversed_phone_book = {}
    result = []
    for command in commands:
        words = command.split()
        if words[0] == 'add':
            name = ''.join(words[2:])
            reversed_phone_book[words[1]] = name
        if words[0] == 'del':
            reversed_phone_book.pop(words[1], None)
        if words[0] == 'find':
            name = reversed_phone_book.get(words[1], 'not found')
            result.append(name)
    return result


def task2():
    data = read_lines(FILE_INPUT, start=1)
    ans = execute(data)
    write_vars(FILE_OUTPUT, *ans)


if __name__ == '__main__':
    task2()
