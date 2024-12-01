from typing import Any


class Stack:

    def __init__(self, size=10**6):
        self.stack = [Any] * size
        self.max_stack = []
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        if self.length < len(self.stack):
            self.stack[self.length] = x
            if self.max_stack == [] or x > self.max_stack[-1][0]:
                self.max_stack.append((x, self.length))
            self.length += 1
        else:
            raise IndexError

    def seek_tail(self):
        return self.stack[self.length - 1]

    def remove(self):
        if self.length - 1 == self.max_stack[-1][1]:
            self.max_stack.pop()
        self.length -= 1

    def pop(self):
        if not self.is_empty():
            res = self.seek_tail()
            self.remove()
            return res
        else:
            raise IndexError

    def seek_max(self):
        return self.max_stack[-1][0]
