# -------------------------------------------------------------
#           Level Order Successor (easy)
# Given a binary tree and a node, find the level order successor of the given node in the tree.
# The level order successor is the node that appears right after the given node in the level order traversal.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
from utils import TreeNode
from collections import deque


def find_successor(root, key):
    que = deque()
    que.append(root)
    while que:
        curr = que.popleft()
        if curr.left:
            que.append(curr.left)
        if curr.right:
            que.append(curr.right)

        if curr.val == key:
            break

    return que.popleft() if que else None


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)
