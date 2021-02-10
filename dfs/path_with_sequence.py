# -------------------------------------------------------------
#           Path With Given Sequence (medium)
# Given a binary tree and a number sequence, find if the sequence
# is present as a root-to-leaf path in the given tree.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
from utils import TreeNode


def find_path(root, sequence):
    if not root:
        return False

    stack = [(root, [root.val])]
    while stack:
        curr, paths = stack.pop()
        if not curr.left and not curr.right:
            if sequence == paths:
                return True

        if curr.left:
            stack.append((curr.left, paths + [curr.left.val]))
        if curr.right:
            stack.append((curr.right, paths + [curr.right.val]))

    return False


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
