from lab4.task2.src.main import task2
from lab4.task4.src.main import task4
from lab4.task5.src.main import task5
from lab4.task12.src.main import task12
from lab3.utils import read_str_lines
import os


TASKS = {2: task2, 4: task4, 5: task5, 12: task12}
current_path = os.path.dirname(os.path.abspath(__file__))


def task_path(task_number):
    return os.path.join(current_path, f'task{task_number}')


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
