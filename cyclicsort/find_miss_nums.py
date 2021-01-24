# -------------------------------------------------------------
#           Find the Duplicate Number (easy)
#
# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
# The array has only one duplicate but it can be repeated multiple times.
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
def find_miss_nums(nums):
    i = 0
    res = []
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(i + 1)

    return res


if __name__ == '__main__':
    print(find_miss_nums(nums=[2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_miss_nums(nums=[2, 4, 1, 2]))
    print(find_miss_nums(nums=[2, 3, 2, 1]))
