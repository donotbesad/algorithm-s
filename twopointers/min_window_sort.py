# -------------------------------------------------------------
#           Minimum Window Sort (medium)
# Given an array, find the length of the smallest subarray in it
# which when sorted will sort the whole array.
#
# Time Complexity: O(nlogn) sort require
# Space Complexity: O(n) to keep sorted arr
# -------------------------------------------------------------
def shortest_window_sort(arr):
    sarr = sorted(arr)
    start, end = len(arr), 0

    for i in range(len(arr)):
        if sarr[i] != arr[i]:
            start = min(start, i)
            end = max(end, i)

    if end - start >= 0:
        return end - start + 1
    else:
        return 0


# Time Complexity: O(n)
# Space Complexity: O(1)
def shortest_window_sort_improved(arr):
    start, end = 0, len(arr) - 1

    while start < len(arr) - 1 and arr[start] <= arr[start + 1]:
        start += 1

    if start == len(arr) - 1:
        return 0

    while end > 0 and arr[end] >= arr[end - 1]:
        end -= 1

    sub_max = float('-inf')
    sub_min = float('inf')
    for i in range(start, end + 1):
        sub_max = max(sub_max, arr[i])
        sub_min = min(sub_min, arr[i])

    while start > 0 and arr[start - 1] > sub_min:
        start -= 1

    while end < len(arr) - 1 and arr[end + 1] < sub_min:
        end += 1

    return end - start + 1


if __name__ == '__main__':
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))
    print('Improved Time O(n) Space O(1)')
    print(shortest_window_sort_improved([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort_improved([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort_improved([1, 2, 3]))
    print(shortest_window_sort_improved([3, 2, 1]))
