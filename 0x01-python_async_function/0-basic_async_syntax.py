#!/usr/bin/env python3
"""
async corutines
"""
import random


async def wait_random(max_delay=10):
    """
    function that returns a random
    num between 0 and max_delay
    """
    rand = await random.uniform(0, max_delay)
    return rand
