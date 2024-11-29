class Queue:

    def __init__(self, size=10**6):
        self.queue = [0] * size
        self.head = 0
        self.tail = 0
        self.is_empty = True
        self.is_full = False

    def add(self, x):
        if self.is_full:
            raise IndexError
        self.queue[self.tail] = x
        if self.tail == len(self.queue):
            self.tail = 0
        else:
            self.tail += 1
        if self.is_empty:
            self.is_empty = False
        if self.tail == self.head:
            self.is_full = True

    def pop(self):
        if self.is_empty:
            raise IndexError
        x = self.queue[self.head]
        if self.head == len(self.queue):
            self.head = 0
        else:
            self.head += 1
        if self.tail == self.head:
            self.is_empty = True
        return x



