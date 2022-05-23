

"""
https://leetcode.com/problems/insert-interval/
"""

def insert(intervals, newInterval):
        res = []
        start=0
        end =1
        for i in range(len(intervals)):
          if intervals[i][start] > newInterval[end]:
            res.append(newInterval)
            return res+intervals[i:]
            
          elif intervals[i][end] < newInterval[start]:
            res.append(intervals[i])
          else:
            newInterval = [min(intervals[i][start],newInterval[start]), max(intervals[i][end],newInterval[end])]
        
        
        res.append(newInterval)
          
        return res



print(insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))