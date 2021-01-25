# -------------------------------------------------------------
#           Find the Duplicate Number (easy)
# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
# The array has only one duplicate but it can be repeated multiple times
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
def find_duplicate(nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            if nums[i] == nums[nums[i]]:
                return nums[i]

    return -1


if __name__ == '__main__':
    print(find_duplicate(nums=[1, 4, 4, 3, 2]))
    print(find_duplicate(nums=[2, 1, 3, 3, 5, 4]))
    print(find_duplicate(nums=[2, 4, 1, 4, 4]))
