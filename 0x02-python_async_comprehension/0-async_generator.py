#!/usr/bin/env python3
"""
async comprehension
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async generator that yields
    random numbers from 0 - 10
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
