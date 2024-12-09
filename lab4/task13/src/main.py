import os
import gc
from lab4.utils import read_lines, write_vars


current_path = os.path.dirname(os.path.abspath(__file__))
file_input = os.path.join(current_path, '../txtf/input.txt')
file_output = os.path.join(current_path, '../txtf/output.txt')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def get_tail(self):
        cur_node = self.head
        if cur_node is None:
            return cur_node
        while cur_node.next is not None:
            cur_node = cur_node.next
        return cur_node

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def push_end(self, x):
        cur_node = self.get_tail()
        if cur_node is None:
            self.push(x)
            return
        new_node = Node(x)
        cur_node.next = new_node
        new_node.prev = cur_node

    @staticmethod
    def insert_after(prev_node: Node, x):
        new_node = Node(x)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    @staticmethod
    def insert_before(next_node: Node, x):
        new_node = Node(x)
        new_node.next = next_node
        prev_node = next_node.prev
        new_node.prev = prev_node
        next_node.prev = new_node
        if prev_node is not None:
            prev_node.next = new_node

    def delete_node(self, x: Node):
        if self.head is None or x is None:
            return
        if self.head == x:
            self.head = x.next
            return
        if x.next.prev is not None:
            x.next.prev = x.prev
        if x.prev is not None:
            x.prev.next = x.next
        gc.collect()

    def get_node(self, data):
        cur_node = self.head
        while cur_node.next is not None:
            if cur_node.data == data:
                return cur_node
            else:
                cur_node = cur_node.next
        if cur_node.data == data:
            return cur_node
        else:
            return None

    def is_empty(self):
        return self.head is None

    def get_list(self):
        node = self.head
        res = []
        while node is not None:
            res.append(node.data)
            node = node.next
        return res

    def print_list(self):
        node = self.head
        last = node
        print('\n Обход в прямом порядке')
        while node is not None:
            print(node.data, end=' ')
            last = node
            node = node.next
        print('\n Обход в обратном порядке')
        while last is not None:
            print(last.data, end=' ')
            last = last.prev


class Stack(DoublyLinkedList):

    def pop(self):
        res = self.head.data
        self.delete_node(self.head)
        return res


if __name__ == '__main__':
    a = DoublyLinkedList()
    a.push(2)
    a.push(1)
    b = Stack()
    b.push(4)
    b.push_end(5)
    b.pop()
    b.pop()
    b.push_end(10)
    b.push(1)
    b.insert_after(b.get_node(1), 5)
    b.insert_before(b.get_node(5), 4)
    pass
