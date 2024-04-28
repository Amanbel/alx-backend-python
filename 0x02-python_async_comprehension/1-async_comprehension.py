#!/usr/bin/env python3
"""
async comprehensions
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async def function that returns the random numbers
    """
    return [_ async for _ in async_generator()]
