# -------------------------------------------------------------
#           Reverse a Sub-list (medium)
# Given the head of a LinkedList and two positions ‘p’ and ‘q’,
# reverse the LinkedList from position ‘p’ to ‘q’.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
from utils import Node


def reverse_sub_list(head, p, q):
    prev = None
    curr = head
    i = 0
    while curr and i < p - 1:
        prev = curr
        curr = curr.next
        i += 1

    p_sub_prev = prev
    p_sub_start = curr

    i = 0
    while curr and i < q - p + 1:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        i += 1

    if p_sub_prev:
        p_sub_prev.next = prev
    else:
        head = prev

    p_sub_start.next = curr
    return head


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
