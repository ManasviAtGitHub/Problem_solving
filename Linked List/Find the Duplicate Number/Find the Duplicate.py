"""
https://leetcode.com/problems/find-the-duplicate-number/
"""

def findDuplicate(nums) -> int:
      
      slow, fast = 0, 0
      
      while True:
        slow = nums[slow]
        
        fast = nums[nums[fast]]
        
        if slow == fast:
          break
        
      
      slow2= 0
      
      while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        
        if slow == slow2:
          return slow



print(findDuplicate(nums = [1,3,4,2,2]))