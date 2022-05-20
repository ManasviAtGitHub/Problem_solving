

"""
https://leetcode.com/problems/jump-game-ii

We take highest possible jump from the previous set, at every iteration
"""

def jump(nums):
        res = 0
        
        left = right = 0
        
        while right<len(nums)-1:
          far = 0
          
          
          for i in range(left, right+1):
            far = max(far, i+nums[i])
          
          left = right+1
          right = far
          
          res+=1
        
        return res



print(jump([2,3,1,1,4]))