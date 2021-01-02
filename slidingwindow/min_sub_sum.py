# -------------------------------------------------------------
#           Smallest Subarray with a given sum (easy)
# Given an array of positive numbers and a positive number ‘S,’
# find the length of the smallest contiguous subarray whose sum
# is greater than or equal to ‘S’. Return 0 if no such subarray exists.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
def min_sub_sum(arr, s):
    window_start = 0
    curr_sum = 0
    min_sub = float('inf')

    for window_end in range(len(arr)):
        curr_sum += arr[window_end]

        while curr_sum >= s:
            min_sub = min(min_sub, window_end - window_start + 1)
            curr_sum -= arr[window_start]
            window_start += 1

    return 0 if min_sub == float('inf') else min_sub


if __name__ == '__main__':
    print(min_sub_sum(arr=[2, 1, 5, 2, 3, 2], s=7))
    print(min_sub_sum(arr=[2, 1, 5, 2, 8], s=1))
    print(min_sub_sum(arr=[], s=1))
    print(min_sub_sum(arr=[3, 4, 1, 1, 6], s=8))
