"""
#52
Google

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. 
If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.

get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.

"""


class LRUCache():
    def __init__(self, capacity):
        self.cache = dict()
        self.orderList = []
        self.capacity = capacity
    
    def set(self, key, value):
        if key in self.cache:
            # Key is in cache, mark it as recently used item.
            self.orderList.remove(key)
            self.orderList.append(key)
        else:
            if len(self.orderList) >= self.capacity:
                # Cache is full, remove least recentyl used item.
                leastRecent = self.orderList.pop(0)
                del self.cache[leastRecent]
            self.orderList.append(key)
        
        # Setting the (new) key and value
        self.cache[key] = value
    
    def get(self, key):
        if key in self.cache:
            # Mark item as recently used
            self.orderList.remove(key)
            self.orderList.append(key)
            return self.cache[key]
        else:
            return -1


def main():
    lruCache = LRUCache(2)
    lruCache.set(1,1)
    lruCache.set(2,2)
    print(lruCache.get(1))
    lruCache.set(3,3)
    print(lruCache.get(2))
    lruCache.set(4,4)
    print(lruCache.get(1))
    print(lruCache.get(3))
    print(lruCache.get(4))    



if __name__ == "__main__":
    main()