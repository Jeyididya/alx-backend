#!/usr/bin/env python3
"""
    Inherit from BaseCache and perform get and put op
"""

BasicCaching = __import__('0-basicCache').BaseCaching


class BasicCache(BasicCaching):
    """
    Put and get methods to deal  with cache
    Methods
        put(item, key)
        get(key)
    """
    def __init__(self):
        """
        init the object and call parent class
        Args
            self
        """
        super().__init__()

    def put(self, key, item):
        """
        insert items to parent class attribute
        Args
            key
            item
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        return item from dictionary
        Args
            key
        """
        if key in self.cache_data.keys() and key:
            return self.cache_data[key]
        return None
