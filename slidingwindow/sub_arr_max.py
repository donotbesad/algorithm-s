# -------------------------------------------------------------
#           Maximum Sum Subarray of Size K (easy)
# Given an array of positive numbers and a positive number ‘k,’
# find the maximum sum of any contiguous subarray of size ‘k’.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# window_start can be implemented as curr_sum -= arr[i - (k - 1)]
# -------------------------------------------------------------
def sub_arr_max(arr, k):
    max_sum = float('-inf')
    curr_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        curr_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[window_start]
            window_start += 1

    return max_sum


if __name__ == '__main__':
    print(sub_arr_max(arr=[2, 1, 5, 1, 3, 2], k=3))
    print(sub_arr_max(arr=[2, 3, 4, 1, 5], k=2))
