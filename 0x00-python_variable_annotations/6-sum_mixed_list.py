#!/usr/bin/env python3
"""
suming up mixed lists
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function that sums up int and float
    """
    return sum(mxd_lst)
