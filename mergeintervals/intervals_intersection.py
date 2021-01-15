# -------------------------------------------------------------
#           Intervals Intersection (medium)
#
# Given two lists of intervals, find the intersection of these two lists.
# Each list consists of disjoint intervals sorted on their start time.
# Time Complexity: O(n)
# Space Complexity: O(1) ignoring result list
# -------------------------------------------------------------
def merge(intervals_a, intervals_b):
    merged = []
    i, j, start, end = 0, 0, 0, 1
    while i < len(intervals_a) and j < len(intervals_b):
        a = intervals_a[i]
        b = intervals_b[j]

        a_overlaps_b = a[start] >= b[start] and a[start] <= b[end]
        b_overlaps_a = b[start] >= a[start] and b[start] <= a[end]

        if a_overlaps_b or b_overlaps_a:
            merged.append([min(a[start], b[start]), max(a[end], b[end])])

        if a[end] <= b[end]:
            i += 1
        else:
            j += 1
    return merged


if __name__ == '__main__':
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))
