# -------------------------------------------------------------
#           Subsets (easy)
# Given a set with distinct elements, find all of its distinct subsets.
#
# Time Complexity: O(N*2^N)
# Space Complexity: O(N*2^N)
# -------------------------------------------------------------
def find_subsets(nums):
    subsets = [[]]
    for curr in nums:
        n = len(subsets)
        for i in range(n):
            subset = list(subsets[i])
            subset.append(curr)
            subsets.append(subset)
    return subsets


if __name__ == '__main__':
    print(find_subsets([1, 3]))
    print(find_subsets([1, 5, 3]))
