# -------------------------------------------------------------
#           Find the Median of a Number Stream (medium)
# Design a class to calculate the median of a number stream. The class should have the following two methods:#
#   insertNum(int num): stores the number in the class
#   findMedian(): returns the median of all numbers inserted in the class
# If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
#
# Time Complexity: O(logN)
# Space Complexity: O(n)
# -------------------------------------------------------------
from heapq import *


class StreamWithSort:
    def __init__(self):
        self.nums = []

    def insert_num(self, num):
        self.nums.append(num)
        self.nums.sort()

    def find_median(self):
        n = len(self.nums)
        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0 if n % 2 == 0 else self.nums[n // 2]


class Stream:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        print(self.min_heap, self.max_heap)
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2.0
        return -float(self.max_heap[0])


if __name__ == '__main__':
    medianOfAStream = Stream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))
