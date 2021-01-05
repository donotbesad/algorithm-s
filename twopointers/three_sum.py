# -------------------------------------------------------------
# Triplet Sum to Zero (medium)
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# -------------------------------------------------------------
def search_triples(nums):
    nums.sort()
    triples = list()
    for curr in range(len(nums)):
        left = curr + 1
        right = len(nums) - 1
        while left < right:
            res = nums[curr] + nums[left] + nums[right]
            if res == 0:
                triples.append([nums[curr], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif res < 0:
                left += 1
            else:
                right -= 1
    return triples


if __name__ == '__main__':
    # [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
    print(search_triples(nums=[-3, 0, 1, 2, -1, 1, -2]))
    # [[-5, 2, 3], [-2, -1, 3]]
    print(search_triples(nums=[-5, 2, -1, -2, 3]))
