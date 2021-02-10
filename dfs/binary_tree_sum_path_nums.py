# -------------------------------------------------------------
#           Sum of Path Numbers (medium)
# Given a binary tree where each node can only have a digit (0-9) value,
# each root-to-leaf path will represent a number. Find the total sum of
# all the numbers represented by all paths.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------

from utils import TreeNode


def find_sum_of_path_numbers(root):
    if not root:
        return 0
    res, all_paths = 0, []
    stack = [(root, str(root.val))]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right:
            all_paths.append(val)
        if curr.left:
            stack.append((curr.left, val + str(curr.left.val)))
        if curr.right:
            stack.append((curr.right, val + str(curr.right.val)))
    for path in all_paths:
        res += int(path)
    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))

    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
