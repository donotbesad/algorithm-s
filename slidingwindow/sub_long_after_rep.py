# -------------------------------------------------------------
#       Longest Substring with Same Letters after Replacement (hard)
# Given a string with lowercase letters only, if you are allowed to replace
# no more than ‘k’ letters with any letter, find the length of the longest
# substring having the same letters after replacement.
#
# Time Complexity: O(n)
# Space Complexity: O(1) fixed set of characters in the alphabet
# -------------------------------------------------------------
def length_of_longest_substring(s, k):
    window_start = 0
    max_length = 0
    max_char_count = 0
    d = dict()

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in d:
            d[right_char] = 0
        d[right_char] += 1
        max_char_count = max(max_char_count, d[right_char])

        if (window_end - window_start + 1 - max_char_count) > k:
            left_char = s[window_start]
            d[left_char] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


if __name__ == '__main__':
    print(length_of_longest_substring(s='aabccbb', k=2))
    print(length_of_longest_substring(s='abbcb', k=1))
    print(length_of_longest_substring(s='abccde', k=1))
