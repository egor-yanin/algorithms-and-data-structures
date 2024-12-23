from lab3.run_tasks import run_task as lab3
from lab4.run_tasks import run_task as lab4
from lab5.run_tasks import run_task as lab5
from lab6.run_tasks import run_task as lab6
from lab7.run_tasks import run_task as lab7


TASK_LIST = {1: [1, 6, 9], 2: [1, 4, 5, 6, 8], 3: [1, 3, 5, 7], 4: [2, 4, 5, 12], 5: [1, 4, 6, 7], 6: [1, 2, 5, 6],
             7: [1, 2, 5, 6]}
LAB_LIST = {3: lab3, 4: lab4, 5: lab5, 6: lab6, 7: lab7}


def run_lab(lub_num):
    print()
    for task_num in TASK_LIST[lub_num]:
        LAB_LIST[lub_num](task_num)


if __name__ == '__main__':
    for lab_num in sorted(LAB_LIST):
        print(f'Лабораторная работа №{lab_num}')
        run_lab(lab_num)
        print('----------------------')
