# -------------------------------------------------------------
#           String Anagrams (hard)
# Given a string and a pattern, find all anagrams of the pattern in the given string.
#
# Time Complexity: O(n + m)
# Space Complexity: O(m)
# -------------------------------------------------------------
def find_string_anagrams(str, pattern):
    start, matched = 0, 0
    chars_frequency = dict()
    res = []

    for char in pattern:
        if char not in chars_frequency:
            chars_frequency[char] = 0
        chars_frequency[char] += 1

    for end in range(len(str)):
        right_char = str[end]
        if right_char in chars_frequency:
            chars_frequency[right_char] -= 1
            if chars_frequency[right_char] == 0:
                matched += 1

        if matched == len(chars_frequency):
            res.append(start)

        if end - start >= len(pattern) - 1:
            left_char = str[start]
            start += 1
            if left_char in chars_frequency:
                if chars_frequency[left_char] == 0:
                    matched -= 1
                chars_frequency[left_char] += 1

    return res


if __name__ == '__main__':
    print(find_string_anagrams(str='ppqp', pattern='pq'))
    print(find_string_anagrams(str='abbcabc', pattern='abc'))
