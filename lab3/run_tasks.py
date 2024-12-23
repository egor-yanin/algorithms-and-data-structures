from lab3.task1.src.main import task1
from lab3.task3.src.main import task3
from lab3.task5.src.main import task5
from lab3.task7.src.main import task7
from lab3.utils import read_str_lines
import os


TASKS = {1: task1, 3: task3, 5: task5, 7: task7}
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def task_path(task_number):
    return os.path.join(CURRENT_DIR, f'task{task_number}')


def run_task(task_number):
    file_input = os.path.join(task_path(task_number), 'txtf/input.txt')
    file_output = os.path.join(task_path(task_number), 'txtf/output.txt')

    print(f'Задача №{task_number}')
    print('Входные данные: ')
    for line in read_str_lines(file_input):
        print(line)
    TASKS[task_number]()
    print('Выходные данные: ')
    for line in read_str_lines(file_output):
        print(line)
    print()


if __name__ == '__main__':
    for task in sorted(TASKS):
        run_task(task)
