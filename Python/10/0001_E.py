#!/usr/bin/python
# coding=utf-8

"""
Problem #1.

Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers
from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

import random


def check_1(n_list: list, k: int) -> bool:
    """
    Solution 1 - Brutal.

    Computationally inefficient.
    """
    for i in range(len(n_list)):
        for j in range(i+1, len(n_list)):
            if n_list[i] + n_list[j] == k:
                return True
    return False


def check_2(n_list: int, k: int) -> bool:
    """
    Solution 2 - Intermediate.

    Computationally inefficient but not as Solution 1.
    """
    n_list.sort()
    for i in range(len(n_list)):
        if n_list[i] > k:
            pass
        else:
            for j in range(i+1, len(n_list)):
                summ = n_list[i] + n_list[j]
                if summ > k:
                    pass
                elif summ == k:
                    return True
    return False


# Solution 3 ==> The Most Efficient
def check_3(n_list: int, k: int) -> bool:
    """
    Solution 3 - Best Solution.

    Computationally efficient.
    """
    b = 0
    e = len(n_list)-1
    n_list.sort()
    while b < e:
        summ = n_list[b] + n_list[e]
        if summ == k:
            return True
        elif summ > k:
            e -= 1
        else:
            b += 1
    return False


if __name__ == "__main__":
    random.seed(0)
    test_vals = ((random.randint(-10, 10), (random.randint(-10, 10)
                 for i in range(10))) for i in range(10))
    for k, l in test_vals:
        expanded = [i for i in l]
        r_1 = check_1(expanded, k)
        r_2 = check_2(expanded, k)
        r_3 = check_3(expanded, k)
        assert r_1 == r_2 == r_3
        print(k, expanded, r_1, r_2, r_3)
