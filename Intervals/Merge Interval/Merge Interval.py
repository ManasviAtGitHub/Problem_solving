"""
https://leetcode.com/problems/merge-intervals/
"""
def merge(intervals):
        
        intervals.sort(key = lambda i :i[0])
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
          
          last = res[-1][1]
          
          
          if start <=last:
            res[-1][1] = max(last, end)
          else:
            res.append([start,end])
          
        return res

print(merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))

