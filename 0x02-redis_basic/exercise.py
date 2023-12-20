#!/usr/bin/env python3
"""write strings"""

import redis
import uuid
from typing import Union

class Cache:
    """store instance od Redis"""
    def __init__(self):
        """Initialize the Cache Creates Redis client and clears the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in the cache and return a unique key"""
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key


    def get_str(self, key: str) -> int:
        """retrieve data as a string from the cache"""
        return self.get(key, str)


    def get_int(self, key: str) -> int:
        """retrieve data as an integer from the cache"""
        return self.get(key, int)
