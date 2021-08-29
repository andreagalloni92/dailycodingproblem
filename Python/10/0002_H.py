#!/usr/bin/python
# coding=utf-8

"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
be [2, 3, 6].

Follow-up: what if you can't use division?
"""

from functools import reduce


def solution_1(n_list: list) -> list:
    """
    Fist Solution.

    Uses division and not super pythonic and not very efficient.
    """
    mult = 1.0
    for i in n_list:
        mult *= i

    res = [mult]*len(n_list)
    for i in range(len(n_list)):
        res[i] /= n_list[i]
    return res


def solution_2(n_list: list) -> list:
    """
    Second Solution.

    Uses division but much more pythonic.
    """
    mult = reduce(lambda x, y: x*y, n_list)
    res = [mult/i for i in n_list]
    return res


def solution_3(n_list: list) -> list:
    """
    Third Solution.

    Does not use division but use more memory.
    It builds partial mutiplication arrays both from left and right.
    I am not sure but I have the feeling there is an even more efficient
    solution.
    """
    temp_l = 1
    temp_r = 1
    left_prod = [1]*len(n_list)
    right_prod = [1]*len(n_list)
    for i in range(0, len(n_list)):
        left_prod[i] = temp_l
        temp_l *= n_list[i]
        right_prod[len(n_list)-(i+1)] = temp_r
        temp_r *= n_list[len(n_list)-(i+1)]

    return [left_prod[i]*right_prod[i] for i in range(len(n_list))]


if __name__ == "__main__":
    res_1 = solution_1([1, 2, 3, 4, 5])
    res_2 = solution_2([1, 2, 3, 4, 5])
    res_3 = solution_3([1, 2, 3, 4, 5])

    assert(res_1 == res_2 == res_3)

    print(res_3)
