#!/usr/bin/env python3
"""
complex types - annotating a function
"""
from typing import Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    """
    annotated function that has been defined
    before hand
    """
    return [(i, len(i)) for i in lst]
