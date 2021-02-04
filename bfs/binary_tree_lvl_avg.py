# -------------------------------------------------------------
#           Level Averages in a Binary Tree (easy)
# Given a binary tree, populate an array to represent the averages of all of its levels.

# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
from utils import TreeNode
from collections import deque


def find_level_averages(root):
    if not root:
        return []

    res, deq = [], deque()
    deq.append(root)
    while deq:
        lvl_size = len(deq)
        curr_lvl_sum = 0
        for _ in range(lvl_size):
            curr = deq.popleft()
            curr_lvl_sum += curr.val
            if curr.left:
                deq.append(curr.left)
            if curr.right:
                deq.append(curr.right)
        res.append(curr_lvl_sum / lvl_size)
    return res


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))
