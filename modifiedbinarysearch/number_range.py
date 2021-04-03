# -------------------------------------------------------------
#           Number Range (medium)
# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’
# will be the first and last position of the ‘key’ in the array.
#
# Time Complexity: O(logn) n=total numbers in array
# Space Complexity: O(1)
# -------------------------------------------------------------
def find_range(nums, target):
    def find_bound(is_first):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                if is_first:
                    if mid == low or nums[mid - 1] != target:
                        return mid
                    high = mid - 1
                else:
                    if mid == high or nums[mid + 1] != target:
                        return mid
                    low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    lower_bound = find_bound(True)
    if lower_bound == -1:
        return [-1, -1]
    upper_bound = find_bound(False)
    return [lower_bound, upper_bound]


if __name__ == '__main__':
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))
