"""
#67
Google

Implement an LFU (Least Frequently Used) cache.
It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. 
If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item.
If there is a tie, then the least recently used key should be removed.

get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
"""


class LFUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.countDict = dict()
        self.grouping = dict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache:
            currentCount = self.countDict[key]
            self.countDict[key] = currentCount+1
            self.grouping[currentCount].remove(key)
            if len(self.grouping[currentCount]) == 0:
                del self.grouping[currentCount]
            if currentCount+1 in self.grouping:
                self.grouping[currentCount+1].append(key)
            else:
                self.grouping[currentCount+1] = [key]
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.cache:
            self.cache[key] = value
            currentCount = self.countDict[key]
            self.countDict[key] = currentCount+1
            self.grouping[currentCount].remove(key)
            if len(self.grouping[currentCount]) == 0:
                del self.grouping[currentCount]
            if currentCount+1 in self.grouping:
                self.grouping[currentCount+1].append(key)
            else:
                self.grouping[currentCount+1] = [key]
        else:
            if len(self.countDict) >= self.capacity:
                lfuCount = min(self.grouping.keys())
                lfuKey = self.grouping[lfuCount].pop(0)
                print(self.grouping[lfuCount])
                if len(self.grouping[lfuCount]) == 0:
                    del self.grouping[lfuCount]
                del self.cache[lfuKey]
                del self.countDict[lfuKey]
            self.cache[key] = value
            if 1 in self.grouping:
                self.grouping[1].append(key)
            else:
                self.grouping[1] = [key]
            self.countDict[key] = 1
    
    def __str__(self):
        return "Capacity: {}\nCache: {}\nCount Dict: {}\nGrouping Dict: {}\n".format(self.capacity, self.cache, self.countDict, self.grouping)


def main():
    lfuCache = LFUCache(2)
    print(lfuCache)
    
    lfuCache.put(1,1)
    print(lfuCache)
    
    lfuCache.put(2,2)
    print(lfuCache)
    
    print(lfuCache.get(1))
    
    lfuCache.put(3,3)
    print(lfuCache)
    
    print(lfuCache.get(2))
    
    print(lfuCache.get(3))
    
    lfuCache.put(4,4)
    print(lfuCache)

    print(lfuCache.get(1))
    
    print(lfuCache.get(3))
    
    print(lfuCache.get(4))


if __name__ == "__main__":
    main()