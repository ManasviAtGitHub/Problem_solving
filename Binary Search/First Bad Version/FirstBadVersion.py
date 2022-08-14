
"""
https://leetcode.com/problems/first-bad-version
"""

def firstBadVersion(self, n: int) -> int:
      
        start = 1
        end = n
        
        
        mid = (start + end)//2
        bad = n
        
        
        for i in range(start, end):
          
          if start > end:
            return bad
          
          if isBadVersion(mid) == True:
            bad = mid
            end = mid - 1
            mid = (start + end)//2
            
            
          elif isBadVersion(mid) == False:
            start = mid + 1
            mid = (start+end)//2
      
      
        return bad