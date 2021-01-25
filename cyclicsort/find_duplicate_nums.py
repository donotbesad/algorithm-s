# -------------------------------------------------------------
#           Find all Duplicate Numbers (easy)
# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
# The array has some numbers appearing twice, find all these duplicate numbers without
# using any extra space.
#
# Time Complexity: O(n)
# Space Complexity: O(1) ignoring output list
# -------------------------------------------------------------
def find_all_duplicates(nums):
    res = []
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            if nums[i] == nums[nums[i] - 1]:
                res.append(nums[i])

    return res


if __name__ == '__main__':
    print(find_all_duplicates(nums=[3, 4, 4, 5, 5]))
    print(find_all_duplicates(nums=[5, 4, 7, 2, 3, 5, 3]))
