# -------------------------------------------------------------
#           Permutation in a String (hard)
# Given a string and a pattern, find out if the string contains
# any permutation of the pattern.
#
# Time Complexity: O(n + m)
# Space Complexity: O(m)
# -------------------------------------------------------------
def find_permutation(str1, pattern):
    start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    for end in range(len(str1)):
        right_char = str1[end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        if end >= len(pattern) - 1:
            left_char = str1[start]
            start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


if __name__ == '__main__':
    print(find_permutation(str1='oidbcaf', pattern='abc'))
    print(find_permutation(str1='odicf', pattern='dc'))
    print(find_permutation(str1='bcdxabcdy', pattern='bcdyabcdx'))
    print(find_permutation(str1='aaacb', pattern='abc'))
    print(find_permutation(str1='ab', pattern='eidbaooo'))
    print(find_permutation(str1='ooolleoooleh', pattern='hello'))
