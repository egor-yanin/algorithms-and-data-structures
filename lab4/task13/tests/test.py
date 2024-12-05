import unittest
from lab4.task13.src.main import DoublyLinkedList, Stack


class TestCase(unittest.TestCase):

    @staticmethod
    def create_doubly_linked_list(lst):
        linked_list = DoublyLinkedList()
        for n in lst:
            linked_list.push(n)
        return linked_list

    @staticmethod
    def create_stack(lst):
        stack = Stack()
        for n in lst:
            stack.push(n)
        return stack

    def test_should_push(self):
        # given
        linked_list = self.create_doubly_linked_list([1, 2, 3])
        expected_result = [3, 2, 1]

        # when
        result = linked_list.get_list()

        # then
        self.assertEqual(result, expected_result)

    def test_should_delete_node(self):
        # given
        linked_list = self.create_doubly_linked_list([1, 2, 3])
        expected_result = [3, 1]

        # when
        linked_list.delete_node(linked_list.get_node(2))

        result = linked_list.get_list()

        # then
        self.assertEqual(result, expected_result)

    def test_should_insert_after(self):
        # given
        linked_list = self.create_doubly_linked_list([1, 2, 3])
        expected_result = [3, 2, 4, 1]

        # when
        linked_list.insert_after(linked_list.get_node(2), 4)
        result = linked_list.get_list()

        # then
        self.assertEqual(result, expected_result)

    def test_should_insert_before(self):
        # given
        linked_list = self.create_doubly_linked_list([1, 2, 3])
        expected_result = [3, 4, 2, 1]

        # when
        linked_list.insert_before(linked_list.get_node(2), 4)
        result = linked_list.get_list()

        # then
        self.assertEqual(result, expected_result)

    def test_should_pop(self):
        # given
        stack = self.create_stack([1, 2, 3])
        expected_result = 3

        # when
        result = stack.pop()

        # then
        self.assertEqual(result, expected_result)
