import unittest
from lab4.task13.src.main import DoublyLinkedList, Stack


class TestCase(unittest.TestCase):

    @staticmethod
    def create_doubly_linked_list(lst):
        res = DoublyLinkedList()
        for n in lst:
            res.push(n)
        return res

    @staticmethod
    def create_stack(lst):
        res = Stack()
        for n in lst:
            res.push(n)
        return res

    def test_should_push(self):
        # given
        temp = self.create_doubly_linked_list([1, 2, 3])
        expected_result = [3, 2, 1]

        # when
        res = temp.get_list()

        # then
        self.assertEqual(res, expected_result)

    def test_should_delete_node(self):
        # given
        temp = self.create_doubly_linked_list([1, 2, 3])
        expected_result = [3, 1]

        # when
        temp.delete_node(temp.get_node(2))

        res = temp.get_list()

        # then
        self.assertEqual(res, expected_result)

    def test_should_insert_after(self):
        # given
        temp = self.create_doubly_linked_list([1, 2, 3])
        expected_result = [3, 2, 4, 1]

        # when
        temp.insert_after(temp.get_node(2), 4)
        res = temp.get_list()

        # then
        self.assertEqual(res, expected_result)

    def test_should_insert_before(self):
        # given
        temp = self.create_doubly_linked_list([1, 2, 3])
        expected_result = [3, 4, 2, 1]

        # when
        temp.insert_before(temp.get_node(2), 4)
        res = temp.get_list()

        # then
        self.assertEqual(res, expected_result)

    def test_should_pop(self):
        # given
        temp = self.create_stack([1, 2, 3])
        expected_result = 3

        # when
        res = temp.pop()

        # then
        self.assertEqual(res, expected_result)
