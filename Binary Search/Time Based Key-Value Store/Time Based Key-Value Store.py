"""
https://leetcode.com/problems/time-based-key-value-store/
"""

class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
          self.keyStore[key] = []
        
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key,[])
        
        l, r = 0, len(values) - 1
        
        while l<=r:
          m = (l+r)//2
          if values[m][1] <= timestamp:
            res = values[m][0]
            l = m+1
          else:
            r = m-1
        
        return res


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
# ["TimeMap", "set", "get", "get", "set", "get", "get"]


# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
obj.set("foo", "bar", 1)

param_2 = obj.get("foo", 1)



print(param_2)