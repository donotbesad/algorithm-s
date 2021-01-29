# -------------------------------------------------------------
#           Reverse a LinkedList (easy)
# Given the head of a Singly LinkedList, reverse the LinkedList.
# Write a function to return the new head of the reversed LinkedList.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
from utils import Node


def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


if __name__ == '__main__':
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
