#!/usr/bin/python3

"""
    Inherit from BaseCache and perform get and put op
"""

BasicCaching = __import__('0-basicCache').BaseCaching


class BasicCache(BasicCaching):
    """
    Put and get methods to deal with cache
    """
    def put(self, key, item):
        if key:
            self.cache_data[key] = item

    def get(self, key):
        if key in self.cache_data.keys() and key:
            return self.cache_data[key]
        return None
