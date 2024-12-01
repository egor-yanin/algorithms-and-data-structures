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
