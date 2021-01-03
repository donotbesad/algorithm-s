# -------------------------------------------------------------
#           Pair with Target Sum (easy)
# Given an array of sorted numbers and a target sum, find a pair
# in the array whose sum is equal to the given target.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------
def pair_with_target_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum > target:
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            return [left, right]
    return []


if __name__ == '__main__':
    print(pair_with_target_sum(arr=[1, 2, 3, 4, 6], target=6))
    print(pair_with_target_sum(arr=[2, 5, 9, 11], target=11))
