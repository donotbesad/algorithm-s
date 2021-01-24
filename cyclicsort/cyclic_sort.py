# -------------------------------------------------------------
#           Cyclic Sort (easy)
# Write a function to sort the objects in-place on their creation
# sequence number in O(n)O(n) and without any extra space.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums


if __name__ == '__main__':
    print(cyclic_sort(nums=[3, 1, 5, 4, 2]))
    print(cyclic_sort(nums=[2, 6, 4, 3, 1, 5]))
    print(cyclic_sort(nums=[1, 5, 6, 4, 3, 2]))
