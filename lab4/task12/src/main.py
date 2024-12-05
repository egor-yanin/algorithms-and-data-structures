import os
from lab4.utils import read_lines, write_vars, print_time_memory


current_path = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_path, '../txtf/input.txt')
file_output = os.path.join(current_path, '../txtf/output.txt')


class Recruit:

    def __init__(self, n=10**3):
        self.formation = [1]
        # self.crowd = list(range(2, n + 1))

    def stand_left(self, i, j):
        j_pos = self.formation.index(j)
        # self.crowd.remove()
        self.formation.insert(j_pos, i)

    def stand_right(self, i, j):
        j_pos = self.formation.index(j)
        self.formation.insert(j_pos + 1, i)

    def leave(self, i):
        self.formation.remove(i)

    def name(self, i):
        i_pos = self.formation.index(i)
        if i_pos == 0:
            left = 0
            right = self.formation[1]
        elif i_pos == len(self.formation):
            left = self.formation[i_pos - 1]
            right = 0
        else:
            left = self.formation[i_pos - 1]
            right = self.formation[i_pos + 1]
        return left, right


def execute(commands: list[str]):
    recruit = Recruit()
    res = []
    for com in commands:
        words = com.split()
        if words[0] == 'left':
            i, j = map(int, words[1:])
            recruit.stand_left(i, j)
        elif words[0] == 'right':
            i, j = map(int, words[1:])
            recruit.stand_right(i, j)
        elif words[0] == 'name':
            i = int(words[1])
            res.append(' '.join(str(x) for x in recruit.name(i)))
        elif words[0] == 'leave':
            i = int(words[1])
            recruit.leave(i)
        else:
            raise ValueError
    return res


@print_time_memory
def task12():
    com_list = read_lines(file_input, start=1)
    ans = execute(com_list)
    write_vars(file_output, *ans)


if __name__ == '__main__':
    task12()
