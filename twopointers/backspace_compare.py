# -------------------------------------------------------------
#           Comparing Strings containing Backspaces (medium)
# Given two strings containing backspaces (identified by the character ‘#’),
# check if the two strings are equal.
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# -------------------------------------------------------------
def backspace_compare(s1, s2):
    def helper(s):
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return stack

    return helper(s1) == helper(s2)


if __name__ == '__main__':
    print(backspace_compare(s1='xy#z', s2='xzz#'))
    print(backspace_compare(s1='xy#z', s2='xyz#'))
    print(backspace_compare(s1='xp#', s2='xyz##'))
    print(backspace_compare(s1='xywrrmp', s2='xywrrmu#p'))
