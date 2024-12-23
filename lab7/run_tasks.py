from lab7.task1.src.main import task1
from lab7.task2.src.main import task2
from lab7.task5.src.main import task5
from lab7.task6.src.main import task6
from lab7.utils import read_lines
import os


TASKS = {1: task1, 2: task2, 5: task5, 6: task6}
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def task_path(task_number):
    return os.path.join(CURRENT_DIR, f'task{task_number}')


def run_task(task_number):
    file_input = os.path.join(task_path(task_number), 'txtf/input.txt')
    file_output = os.path.join(task_path(task_number), 'txtf/output.txt')

    print(f'Задача №{task_number}')
    print('Входные данные: ')
    for line in read_lines(file_input):
        print(line)
    TASKS[task_number]()
    print('Выходные данные: ')
    for line in read_lines(file_output):
        print(line)
    print()


if __name__ == '__main__':
    for task in sorted(TASKS):
        run_task(task)
