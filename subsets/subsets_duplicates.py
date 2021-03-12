# -------------------------------------------------------------
#           Subsets With Duplicates (easy)
# Given a set of numbers that might contain duplicates, find all of its distinct subsets.
#
# Time Complexity: O(n2^n)
# Space Complexity: O(n2^n)
# -------------------------------------------------------------
def find_subsets(nums):
    nums.sort()
    subsets = [[]]
    end = 0
    for i in range(len(nums)):
        start = 0
        if i > 0 and nums[i] == nums[i - 1]:
            start = end + 1
        end = len(subsets) - 1
        for j in range(start, end + 1):
            subset = list(subsets[j])
            subset.append(nums[i])
            subsets.append(subset)
    return subsets


if __name__ == '__main__':
    print(find_subsets([1, 3, 3]))
    print(find_subsets([1, 5, 3, 3]))
