#!/usr/bin/env python3
"""
complex types - returning str and float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    functions that returns a tuple of str and int/float
    """
    return (k, v**2)
