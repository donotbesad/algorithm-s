# -------------------------------------------------------------
#           Squaring a Sorted Array (easy)
# Given a sorted array, create a new array containing squares of
# all the numbers of the input array in the sorted order.

# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    left = 0
    right = n - 1
    highest_idx = n - 1
    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            squares[highest_idx] = left_square
            left += 1
        else:
            squares[highest_idx] = right_square
            right -= 1
        highest_idx -= 1
    return squares


if __name__ == '__main__':
    # [0, 1, 4, 4, 9]
    print(make_squares(arr=[-2, -1, 0, 2, 3]))
    # [0, 1, 1, 4, 9]
    print(make_squares(arr=[-3, -1, 0, 1, 2]))
