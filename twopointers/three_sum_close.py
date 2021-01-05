# -------------------------------------------------------------
#           Triplet Sum Close to Target (medium)
# Given an array of unsorted numbers and a target number, find a triplet
# in the array whose sum is as close to the target number as possible, return
# the sum of the triplet.
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# -------------------------------------------------------------
def three_sum_close(arr, target_sum):
    arr.sort()
    diff = float('inf')
    for curr in range(len(arr)):
        left = curr + 1
        right = len(arr) - 1
        while left < right:
            sum = arr[curr] + arr[left] + arr[right]

            if abs(target_sum - sum) < abs(diff):
                diff = target_sum - sum

            if sum < target_sum:
                left += 1
            elif sum > target_sum:
                right -= 1
            else:
                break

    return target_sum - diff


if __name__ == '__main__':
    print(three_sum_close(arr=[-2, 0, 1, 2], target_sum=2))  # 1
    print(three_sum_close(arr=[-3, -1, 1, 2], target_sum=1))  # 0
    print(three_sum_close(arr=[1, 0, 1, 1], target_sum=100))  # 3
