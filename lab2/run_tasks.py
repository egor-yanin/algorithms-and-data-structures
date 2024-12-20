from lab2.task1.src.main import task1
from lab2.task4.src.main import task4
from lab2.task5.src.main import task5
from lab2.task6.src.main import task6
from lab2.task8.src.main import task8
from lab2.utils import read_lines
import os


TASKS = {1: task1, 4: task4, 5: task5, 6: task6, 8: task8}
current_path = os.path.dirname(os.path.abspath(__file__))


def task_path(task_number):
    return os.path.join(current_path, f'task{task_number}')


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
