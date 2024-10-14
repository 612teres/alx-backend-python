#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    '''Simulates a delay of random duration up to max_delay seconds.'''
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay