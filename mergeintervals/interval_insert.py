# -------------------------------------------------------------
#           Insert Interval (medium)
# Given a list of non-overlapping intervals sorted by their start time,
# insert a given interval at the correct position and merge all necessary
# intervals to produce a list that has only mutually exclusive intervals.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------------------------------------
def insert(intervals, new_interval):
    res = []
    i = 0
    start = 0
    end = 1

    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        res.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

    res.append([new_interval[start], new_interval[end]])

    while i < len(intervals):
        res.append(intervals[i])
        i += 1

    return res


if __name__ == '__main__':
    # [[1,3], [4,7], [8,12]]
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    # [[1,3], [4,12]]
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    # [[1,4], [5,7]]
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))
