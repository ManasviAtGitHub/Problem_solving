"""
https://leetcode.com/problems/find-pivot-index
"""

def pivotIndex(nums):
      
      maxsum = sum(nums)
      
      leftsum = 0
      for i, x in enumerate(nums):
          if leftsum == (maxsum - leftsum - x):
              return i
          leftsum += x
            
      return -1

print(pivotIndex(nums = [1,7,3,6,5,6]))