
"""
https://leetcode.com/problems/running-sum-of-1d-array
"""
def runningSum(nums):
      
      k = 1
      for i in nums:
        if k < len(nums):
          nums[k]+=i
          k+=1
      return nums


print(runningSum([1,2,3,4]))