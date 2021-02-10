# -------------------------------------------------------------
#           Binary tree path maximum sum (easy)
# Given a binary tree, find the root-to-leaf path with the maximum sum.
#
# Time Complexity: O(n)
# Space Complexity: O(h) as h is the deepest path in the bt
# -------------------------------------------------------------
from utils import TreeNode


def find_max_path_iterative(root):
    if not root:
        return 0

    max_sum = 0
    stack = [(root, root.val)]
    while stack:
        curr, sum = stack.pop()
        if not curr.left and not curr.right:
            max_sum = max(max_sum, sum)
        if curr.left:
            stack.append((curr.left, sum + curr.left.val))
        if curr.right:
            stack.append((curr.right, sum + curr.right.val))
    return max_sum


def find_max_path(root):
    return find_recursive(root)


def find_recursive(curr):
    if not curr:
        return 0
    left = find_recursive(curr.left)
    right = find_recursive(curr.right)
    return max(left, right) + curr.val


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree paths : " + str(find_max_path(root)))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.right.left = TreeNode(10)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(9)
    root.right.right.right = TreeNode(5)
    print("Tree paths : " + str(find_max_path(root)))
