# -------------------------------------------------------------
#           Start of LinkedList Cycle (medium)
# Given the head of a Singly LinkedList that contains a cycle,
# write a function to find the starting node of the cycle.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
from fastslowpointer.Node import Node


def find_cycle_start(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            new_slow = head
            while new_slow != slow:
                slow = slow.next
                new_slow = new_slow.next
            return slow
    return None


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))
