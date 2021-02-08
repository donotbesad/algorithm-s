# -------------------------------------------------------------
#           Binary Tree Paths (easy)
# Given a binary tree, return all root-to-leaf paths.
#
# Time Complexity: O(n)
# Space Complexity: O(h) as h is the deepest path in the bt
# -------------------------------------------------------------
from utils import TreeNode


def find_paths_iterative(root):
    if not root:
        return []

    all_paths = []
    stack = [(root, [root.val])]
    while stack:
        curr, paths = stack.pop()
        if not curr.left and not curr.right:
            all_paths.append(paths)
        if curr.left:
            stack.append((curr.left, paths + [curr.left.val]))
        if curr.right:
            stack.append((curr.right, paths + [curr.right.val]))
    return all_paths


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree paths : " + str(find_paths_iterative(root)))
