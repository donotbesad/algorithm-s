# -------------------------------------------------------------
#           Binary Tree Level Order Traversal (easy)
# Given a binary tree, populate an array to represent its level-by-level traversal.
# You should populate the values of all nodes of each level from left to right in separate sub-arrays.
#
# Time Complexity: O(n)
# Space Complexity: O(n) since we need to store results
# -------------------------------------------------------------
from utils import TreeNode
from collections import deque


def traverse(root):
    res, queue = [], deque([])
    queue.append(root)
    while queue:
        lvl_size = len(queue)
        curr_lvl = []
        for _ in range(lvl_size):
            curr = queue.popleft()
            curr_lvl.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        res.append(curr_lvl)
    return res


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))
