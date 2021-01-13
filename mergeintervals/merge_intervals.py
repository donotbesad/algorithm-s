# -------------------------------------------------------------
#           Merge Intervals (medium)
# Given a list of intervals, merge all the overlapping intervals
# to produce a list that has only mutually exclusive intervals.
#
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# -------------------------------------------------------------
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    if not intervals:
        return []
    if len(intervals) == 1:
        return intervals
    merged = []
    intervals.sort(key=lambda x: x.start)
    start = intervals[0].start
    end = intervals[0].end
    for il in range(1, len(intervals)):
        interval = intervals[il]
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end
    merged.append(Interval(start, end))
    return merged


if __name__ == '__main__':
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]):
        i.print_interval()