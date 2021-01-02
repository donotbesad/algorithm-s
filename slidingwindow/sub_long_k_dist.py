# -------------------------------------------------------------
#       Longest Substring with K Distinct Characters (medium)
# Given a string, find the length of the longest substring in it with
# no more than K distinct characters.
#
# Time Complexity: O(n) (n+n)
# Space Complexity: O(n) (k)
# -------------------------------------------------------------
def longest_sub_k_dist(s, k):
    window_start = 0
    max_length = float('-inf')
    d = dict()

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in d:
            d[right_char] = 0
        d[right_char] += 1

        left_char = s[window_start]
        if len(d) > k:
            d[left_char] -= 1
            if d[left_char] == 0:
                del d[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


if __name__ == '__main__':
    print(longest_sub_k_dist(s='araaci', k=2))
    print(longest_sub_k_dist(s='araaci', k=1))
    print(longest_sub_k_dist(s='cbbebi', k=3))
    print(longest_sub_k_dist(s='', k=1))
