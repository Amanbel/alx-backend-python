#!/usr/bin/env python3
""" suming up mixed lists """
from typing import List


def sum_mixed_list(mxd_lst: List[float, int]) -> float:
    """ function that sums up int and float """
    return sum(mxd_lst)
