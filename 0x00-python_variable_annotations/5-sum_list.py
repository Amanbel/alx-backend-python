#!/usr/bin/env python3
""" summing up floats """

type FloatList = list[float]


def sum_list(input_list: FloatList) -> float:
    """ function that returns the sum
    of the lists """
    sum: float = 0
    for i in range(0, len(input_list) - 1):
        sum += input_list[i]
    return sum
