# -------------------------------------------------------------
#           No-repeat Substring (hard)
# Given a string, find the length of the longest substring, which
# has no repeating characters.
#
# Time Complexity: O(n)
# Space Complexity: O(1) fixed set of characters in the alphabet
# -------------------------------------------------------------
def non_repeat_substring(s):
    window_start = 0
    max_length = 0
    d = dict()

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in d:
            window_start = max(window_start, d[right_char] + 1)
            del d[right_char]
        d[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


if __name__ == '__main__':
    print(non_repeat_substring(s='aabccbb'))
    print(non_repeat_substring(s='abbbb'))
    print(non_repeat_substring(s='abccde'))
    print(non_repeat_substring(s='abcabcbb'))
    print(non_repeat_substring(s='abba'))
