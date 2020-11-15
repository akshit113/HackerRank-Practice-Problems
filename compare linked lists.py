#!/bin/python3


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)


# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    curr1 = llist1
    curr2 = llist2
    is_equal = 1
    while True:
        if (curr1 is None) & (curr2 is not None):
            is_equal = 0
            break

        elif (curr2 is None) & (curr1 is not None):
            is_equal = 0
            break
        elif (curr1 is None) & (curr2 is None):
            break

        elif curr1.data == curr2.data:
            curr1 = curr1.next
            curr2 = curr2.next
        else:
            is_equal = 0
            break

    return is_equal


if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
        print_singly_linked_list(llist1.head, sep=' ')
        print_singly_linked_list(llist2.head, sep=' ')

        result = compare_lists(llist1.head, llist2.head)

        print(str(int(result)) + '\n')
