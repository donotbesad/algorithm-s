# -------------------------------------------------------------
#           Remove Duplicates (easy)
# Given an array of sorted numbers, remove all duplicates from it.
# You should not use any extra space; after removing the duplicates i
# n-place return the length of the subarray that has no duplicate in it.

# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
def remove_duplicates(arr):
    if not arr:
        return 0

    slow = 0
    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1


if __name__ == '__main__':
    print(remove_duplicates(arr=[2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates(arr=[2, 2, 2, 11]))
