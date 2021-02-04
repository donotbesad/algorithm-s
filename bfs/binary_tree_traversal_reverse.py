# -------------------------------------------------------------
#           Reverse Level Order Traversal (easy)
# Given a binary tree, populate an array to represent its level-by-level traversal
# in reverse order, i.e., the lowest level comes first. You should populate the values
# of all nodes in each level from left to right in separate sub-arrays.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
from collections import deque

from utils import TreeNode


def traverse(root):
    res, que = deque(), deque()
    que.append(root)
    while que:
        lvl_size = len(que)
        curr_lvl = []
        for _ in range(lvl_size):
            curr = que.popleft()
            curr_lvl.append(curr.val)
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
        res.appendleft(curr_lvl)
    return res


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))
