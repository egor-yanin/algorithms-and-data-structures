from lab3.run_tasks import run_task as lab3


TASK_LIST = {1: [1, 6, 9], 2: [1, 4, 5, 6, 8], 3: [1, 3, 5, 7]}
LAB_LIST = {3: lab3}


def run_lab(lub_num):
    for task_num in TASK_LIST[lub_num]:
        LAB_LIST[lub_num](task_num)


if __name__ == '__main__':
    for lab_num in sorted(LAB_LIST):
        print(f'Лабораторная работа №{lab_num}')
        run_lab(lab_num)
        print()
