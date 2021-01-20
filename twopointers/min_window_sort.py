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


if __name__ == '__main__':
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))
