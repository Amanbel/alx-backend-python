#!/usr/bin/env python3
"""
measures the runtime
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures the runtime of the async_comprehension
    by running multiple calls in parallel and then
    returning the total
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension()
                        , async_comprehension(), async_comprehension())
    return time.perf_counter() - start_time