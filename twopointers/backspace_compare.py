# -------------------------------------------------------------
#           Comparing Strings containing Backspaces (medium)
# Given two strings containing backspaces (identified by the character ‘#’),
# check if the two strings are equal.
#
# Time Complexity: O(s + t)
# Space Complexity: O(s + t)
# -------------------------------------------------------------
def backspace_compare(S, T):
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

    return helper(S) == helper(T)

# Follow up: Can you solve it in O(N) time and O(1) space?
def backspace_compare_constant_space(S, T):
    i = len(S) - 1
    j = len(T) - 1

    while i >= 0 or j >= 0:
        bs_count = 0
        while i >= 0:
            if S[i] == '#':
                bs_count += 1
            elif bs_count > 0:
                bs_count -= 1
            else:
                break
            i -= 1

        bs_count = 0
        while j >= 0:
            if T[j] == '#':
                bs_count += 1
            elif bs_count > 0:
                bs_count -= 1
            else:
                break
            j -= 1

        if i < 0 and j < 0:
            return True

        if i < 0 or j < 0:
            return False

        if S[i] != T[j]:
            return False

        i -= 1
        j -= 1

    return True


if __name__ == '__main__':
    print(backspace_compare(S='xy#z', T='xzz#'))
    print(backspace_compare(S='xy#z', T='xyz#'))
    print(backspace_compare(S='xp#', T='xyz##'))
    print(backspace_compare(S='xywrrmp', T='xywrrmu#p'))
    print('Space O(1)')
    print(backspace_compare_constant_space(S='xy#z', T='xzz#'))
    print(backspace_compare_constant_space(S='xy#z', T='xyz#'))
    print(backspace_compare_constant_space(S='xp#', T='xyz##'))
    print(backspace_compare_constant_space(S='xywrrmp', T='xywrrmu#p'))
