import collections


# popitem, move_to_endの計算量はそれぞれO(1)
class LRUCache:
    def __init__(self, limit):
        self.limit = limit
        self.cacheDict = collections.OrderedDict()
    
    def put(self, key, value):
        if key in self.cacheDict:
            self.cacheDict.pop(key) # 既に存在する場合は、参照カウントをリセットするために一度削除
        elif len(self.cacheDict) >= self.limit:
            self.cacheDict.popitem(last=False)
        self.cacheDict[key] = value
    
    def get(self, key):
        if key in self.cacheDict:
            self.cacheDict.move_to_end(key)
            return self.cacheDict[key]
        return -1
