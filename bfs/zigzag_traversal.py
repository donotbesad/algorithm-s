# -------------------------------------------------------------
#           Zigzag Traversal (medium)
# Given a binary tree, populate an array to represent its zigzag level order traversal.
# You should populate the values of all nodes of the first level from left to right, then
# right to left for the next level and keep alternating in the same manner for the following levels.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
from collections import deque

from utils import TreeNode


def traverse(root):
    if not root:
        return []

    res, que = [], deque()
    que.append(root)
    left_to_right = True
    while que:
        lvl_size = len(que)
        curr_lvl = deque()
        for _ in range(lvl_size):
            curr = que.popleft()
            if left_to_right:
                curr_lvl.append(curr.val)
            else:
                curr_lvl.appendleft(curr.val)

            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
        left_to_right = not left_to_right
        res.append(list(curr_lvl))
    return res


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))
