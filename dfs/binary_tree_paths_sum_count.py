# -------------------------------------------------------------
#           Count Paths for a Sum (medium)
# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all
# the node values of each path equals ‘S’. Please note that the paths can start or end at any
# node but all paths must follow direction from parent to child (top to bottom).
#
# Time Complexity: O(n) worst case is O(n^2) if binary tree is not balanced
# Space Complexity: O(n)
# -------------------------------------------------------------
from utils import TreeNode


def count_paths_recursive(curr_node, s, curr_path):
    if not curr_node:
        return 0

    curr_path.append(curr_node.val)
    count, sum = 0, 0
    for i in reversed(range(len(curr_path))):
        sum += curr_path[i]
        if sum == s:
            count += 1

    count += count_paths_recursive(curr_node.left, s, curr_path)
    count += count_paths_recursive(curr_node.right, s, curr_path)

    curr_path.pop()

    return count


def count_paths(root, S):
    if not root:
        return 0
    count = 0
    stack = [(root, [root.val])]
    while stack:
        curr, paths = stack.pop()

        if not curr.left and not curr.right:
            start = 0
            sum = 0
            for end in range(len(paths)):
                sum += paths[end]
                if sum > S:
                    sum -= paths[start]
                    start += 1
                if sum == S:
                    count += 1

        if curr.left:
            stack.append((curr.left, paths + [curr.left.val]))
        if curr.right:
            stack.append((curr.right, paths + [curr.right.val]))

    return count


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))
    print("Tree has paths: " + str(count_paths_recursive(root, 11, [])))
