# -------------------------------------------------------------
#   Reverse the first ‘k’ elements of a given LinkedList. (medium)
# Reverse the first ‘k’ elements of a given LinkedList.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
from utils import Node


def reverse_k_sub_list(head, k):
    sub_k_start = head
    prev = None
    curr = head

    i = 0
    while curr and i < k:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        i += 1

    sub_k_start.next = curr
    return prev


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_k_sub_list(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
