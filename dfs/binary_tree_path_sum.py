# -------------------------------------------------------------
#           Binary Tree Path Sum (easy)
# Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf
# such that the sum of all the node values of that path equals ‘S’.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
from utils import TreeNode


def has_path(root, sum):
    if not root:
        return False

    if root.val == sum and root.left is None and root.right is None:
        return True

    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def has_path_iterative(root, sum):
    if not root:
        return False
    stack = [(root, root.val)]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right and val == sum:
            return True
        if curr.left:
            stack.append((curr.left, val + curr.left.val))
        if curr.right:
            stack.append((curr.right, val + curr.right.val))
    return False


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path iterative: " + str(has_path_iterative(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))
    print("Tree has path iterative: " + str(has_path_iterative(root, 16)))
