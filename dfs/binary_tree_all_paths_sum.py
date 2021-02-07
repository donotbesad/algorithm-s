# -------------------------------------------------------------
#           All Paths for a Sum (medium)
# Given a binary tree and a number ‘S’, find all paths from root-to-leaf
# such that the sum of all the node values of each path equals ‘S’.
#
# Time Complexity: O(n)
# Space Complexity: O(h) as h is the deepest path in the bt
# -------------------------------------------------------------
from utils import TreeNode


def find_paths_iterative(root, sum):
    all_paths = []
    stack = [(root, sum - root.val, [root.val])]
    while stack:
        curr, val, paths = stack.pop()
        if not curr.left and not curr.right and val == 0:
            all_paths.append(paths)
        if curr.right:
            stack.append((curr.right, val - curr.right.val, paths + [curr.right.val]))
        if curr.left:
            stack.append((curr.left, val - curr.left.val, paths + [curr.left.val]))
    return all_paths


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths_iterative(root, sum)))
