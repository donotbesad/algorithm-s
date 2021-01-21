# -------------------------------------------------------------
#           Rearrange a LinkedList (medium)
# Given the head of a Singly LinkedList, write a method to modify the LinkedList
# such that the nodes from the second half of the LinkedList are inserted alternately
# to the nodes from the first half in reverse order.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
from fastslowpointer.Node import Node


def reorder(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    first = head
    second = prev

    while first and second:
        tmp = first.next
        first.next = second
        first = tmp

        tmp = second.next
        second.next = first
        second = tmp

    if first:
        first.next = None


if __name__ == '__main__':
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()
