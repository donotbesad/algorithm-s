# -------------------------------------------------------------
# Given a set of intervals, find out if any two intervals overlap.
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# -------------------------------------------------------------
def intervals_overlap(intervals):
    intervals.sort(key=lambda x: x[0])
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        istart = intervals[i][0]
        iend = intervals[i][1]
        if istart <= end:
            return True
        else:
            end = iend
    return False


if __name__ == '__main__':
    print(intervals_overlap([[1, 4], [2, 5], [7, 9]]))
    print(intervals_overlap([[1, 4], [5, 7], [8, 9]]))
