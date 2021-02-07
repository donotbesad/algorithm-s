# -------------------------------------------------------------
#           Connect Level Order Siblings (medium)
# Given a binary tree, connect each node with its level order successor.
# The last node of each level should point to a null node.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
from utils import TreeNode
from collections import deque


def connect_level_order_siblings(root):
    if not root:
        return root

    que = deque()
    que.append(root)
    while que:
        lvl_size = len(que)
        prev = None
        for _ in range(lvl_size):
            curr = que.popleft()
            if prev:
                prev.next = curr
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
            prev = curr
        prev.next = TreeNode(-1)


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()
