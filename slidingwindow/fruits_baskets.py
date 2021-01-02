# -------------------------------------------------------------
#           Fruits into Baskets (medium)
#
# Given an array of characters where each character represents a fruit tree,
# you are given two baskets, and your goal is to put maximum number of fruits
# in each basket. The only restriction is that each basket can have only one type of fruit.
#
# Time Complexity: O(n) (n+n)
# Space Complexity: O(1)
# -------------------------------------------------------------
def fruits_into_baskets(fruits):
    window_start = 0
    basket = dict()
    max_fruits = float('-inf')

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]

        if right_fruit not in basket:
            basket[right_fruit] = 0
        basket[right_fruit] += 1

        if len(basket) > 2:
            left_fruit = fruits[window_start]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            window_start += 1
        max_fruits = max(max_fruits, window_end - window_start + 1)

    return max_fruits


if __name__ == '__main__':
    print(fruits_into_baskets(fruits=['A', 'B', 'C', 'A', 'C']))
    print(fruits_into_baskets(fruits=['A', 'B', 'C', 'B', 'B', 'C']))
