#!/usr/bin/env python3
"""
complex types - returning a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a function that returns a function to
    be multiplyed by the float argument
    """
    def multiply(n: float) -> float:
        """
        the returned function
        """
        return n * multiplier
    return multiply
