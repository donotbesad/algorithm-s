# -------------------------------------------------------------
#           Longest Subarray with Ones after Replacement (hard)
# Given an array containing 0s and 1s, if you are allowed to replace
# no more than ‘k’ 0s with 1s, find the length of the longest contiguous
# subarray having all 1s.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
def max_ones(arr, k):
    window_start = 0
    max_ones_count = 0
    max_length = 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


if __name__ == '__main__':
    print(max_ones(arr=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2))
    print(max_ones(arr=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3))
