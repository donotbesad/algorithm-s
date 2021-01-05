# -------------------------------------------------------------
#           Triplets with Smaller Sum (medium)
# Given an array arr of unsorted numbers and a target sum, count
# all triplets in it such that arr[i] + arr[j] + arr[k] < target
# where i, j, and k are three different indices.
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# -------------------------------------------------------------
def triplet_with_smaller_sum(arr, target):
    arr.sort()
    res = list()
    for curr in range(len(arr)):
        left = curr + 1
        right = len(arr) - 1
        while left < right:
            if arr[curr] + arr[left] + arr[right] < target:
                for i in range(right, left, -1):
                    res.append([arr[curr], arr[left], arr[i]])
                # res += right - left
                left += 1
            else:
                right -= 1
    return res


if __name__ == '__main__':
    print(triplet_with_smaller_sum(arr=[-1, 0, 2, 3], target=3))
    print(triplet_with_smaller_sum(arr=[-1, 4, 2, 1, 3], target=5))
