# -------------------------------------------------------------
#           Find the Missing Number (easy)
# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
# Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
def find_miss_num(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return len(nums)


if __name__ == '__main__':
    print(find_miss_num(nums=[4, 0, 3, 1]))
    print(find_miss_num(nums=[8, 3, 5, 2, 4, 6, 0, 1]))
