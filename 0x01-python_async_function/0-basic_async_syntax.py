#!/usr/bin/env python3
"""
async corutines
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    function that returns a random
    num between 0 and max_delay
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
