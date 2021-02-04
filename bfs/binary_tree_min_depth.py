# -------------------------------------------------------------
#           Minimum Depth of a Binary Tree (easy)
# Find the minimum depth of a binary tree. The minimum depth is the number of nodes
# along the shortest path from the root node to the nearest leaf node.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
from utils import TreeNode
from collections import deque


def find_minimum_depth(root):
    res, deq = [], deque()
    deq.append(root)
    lvl_count = 0
    while deq:
        lvl_count += 1
        for _ in range(len(deq)):
            curr = deq.popleft()
            if not curr.left and not curr.right:
                return lvl_count
            if curr.left:
                deq.append(curr.left)
            if curr.right:
                deq.append(curr.right)


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
