# -------------------------------------------------------------
# Time Complexity: O(?)
# Space Complexity: O(?)
# -------------------------------------------------------------
from utils import Node


def reverse_sub_list(head, p, q):
    curr = head
    prev = None
    while curr and curr.value != p:
        prev = curr
        curr = curr.next

    while curr and curr.value != q:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return curr


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
