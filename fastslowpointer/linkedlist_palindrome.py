# -------------------------------------------------------------
#           Palindrome LinkedList (medium)
# Given the head of a Singly LinkedList, write a method to check
# if the LinkedList is a palindrome or not.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
from fastslowpointer.Node import Node


def is_palindromic_linked_list(head):
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

    slow = head
    while prev:
        if prev.value != slow.value:
            return False
        prev = prev.next
        slow = slow.next
    return True


if __name__ == '__main__':
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))
