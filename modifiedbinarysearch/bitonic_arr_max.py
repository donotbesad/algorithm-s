# -------------------------------------------------------------
#           Bitonic Array Maximum (easy)
# Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing
# and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array
# arr[i] != arr[i+1].
# Time Complexity: O(logn)
# Space Complexity: O(1)
# -------------------------------------------------------------
def find_max_in_bitonic_array(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return arr[low]


if __name__ == '__main__':
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))
