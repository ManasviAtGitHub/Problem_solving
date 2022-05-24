"""
https://leetcode.com/problems/container-with-most-water/
"""

def maxArea(height):
        l, r = 0, len(height)-1
        
        res =0
        
        while l<r:
          
          res = max(res, (r-l) * min(height[l], height[r]))
          
          if height[l]< height[r]:
            l+=1
          else:
            r-=1
          
        return res


print(maxArea(height = [1,8,6,2,5,4,8,3,7]))