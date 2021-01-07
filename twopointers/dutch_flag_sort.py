# -------------------------------------------------------------
#           Dutch National Flag Problem (medium)
# Given an array containing 0s, 1s and 2s, sort the array in-place.
# You should treat numbers of the array as objects, hence, we can’t
# count 0s, 1s, and 2s to recreate the array.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
def dutch_flag_sort(arr):
    left = 0
    right = len(arr) - 1
    i = 0
    while i <= right:
        if arr[i] == 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:  # arr[i] == 2
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
    return arr


if __name__ == '__main__':
    print(dutch_flag_sort(arr=[1, 0, 2, 1, 0]))
    print(dutch_flag_sort(arr=[2, 2, 0, 1, 2, 0]))