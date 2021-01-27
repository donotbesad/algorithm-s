# -------------------------------------------------------------
#           Find the Smallest Missing Positive Number (medium)
# Given an unsorted array containing numbers, find the smallest missing positive number in it.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
def find_first_miss_positive(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == '__main__':
    print(find_first_miss_positive(nums=[-3, 1, 5, 4, 2]))
    print(find_first_miss_positive(nums=[3, -2, 0, 1, 2]))
    print(find_first_miss_positive(nums=[3, 2, 5, 1]))
    print(find_first_miss_positive(nums=[7, 8, 9, 11, 12]))
