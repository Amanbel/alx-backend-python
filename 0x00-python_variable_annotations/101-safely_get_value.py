#!/usr/bin/env python3
"""
Complex types - generic types
"""
from typing import Mapping, TypeVar, Union, Any
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    annotated predefined function
    """
    if key in dct:
        return dct[key]
    else:
        return default
