# -------------------------------------------------------------
#           Reverse every K-element Sub-list (medium)
# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’
# sized sub-list starting from the head. If, in the end, you are left
# with a sub-list with less than ‘k’ elements, reverse it too.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
from utils import Node


def reverse(head, count):
    prev = None
    curr = head
    while count > 0:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        count -= 1
    return curr, prev


# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
def reverse_k_group(head, k):
    count = 0
    curr = head
    while curr and count < k:
        curr = curr.next
        count += 1
    if count < k:
        return head
    new_head, prev = reverse(head, count)
    head.next = reverse_k_group(new_head, k)
    return prev


def reverse_k_group_with_last(head, k):
    count = 0
    curr = head
    while curr and count < k:
        curr = curr.next
        count += 1
    new_head, prev = reverse(head, count)
    if count < k:
        return prev
    head.next = reverse_k_group_with_last(new_head, k)
    return prev


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_k_group(head, 3)
    print("Nodes of reversed without reversing last group LinkedList are: ", end='')
    result.print_list()

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_k_group_with_last(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
