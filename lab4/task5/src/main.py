from typing import Any


class Stack:

    def __init__(self, size=10**6):
        self.stack = [Any] * size
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def add(self, x):
        if self.length < len(self.stack):
            self.stack[self.length] = x
            self.length += 1
        else:
            raise IndexError

    def seek_tail(self):
        return self.stack[self.length - 1]

    def remove(self):
        self.length -= 1

    def pop(self):
        if not self.is_empty():
            res = self.seek_tail()
            self.remove()
            return res
        else:
            raise IndexError
