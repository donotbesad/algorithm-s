# -------------------------------------------------------------
#           Quadruple Sum to Target (medium) ? (hard...)
# Given an array of unsorted numbers and a target number, find all unique
# quadruplets in it, whose sum is equal to the target number.
#
# Time Complexity: O(n^3)
# Space Complexity: O(n)
# -------------------------------------------------------------
def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []
    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        a = arr[i]
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            b = arr[j]
            left = j + 1
            right = len(arr) - 1
            while left < right:
                c = arr[left]
                d = arr[right]
                sum = a + b + c + d
                if sum == target:
                    quadruplets.append([a, b, c, d])
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1
    return quadruplets


if __name__ == '__main__':
    # [-3, -1, 1, 4], [-3, 1, 1, 2]
    print(search_quadruplets(arr=[4, 1, 2, -1, 1, -3], target=1))
    # [-2, 0, 2, 2], [-1, 0, 1, 2]
    print(search_quadruplets(arr=[2, 0, -1, 1, -2, 2], target=2))
