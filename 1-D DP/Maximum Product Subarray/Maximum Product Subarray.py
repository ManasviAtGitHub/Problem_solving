
"""
https://leetcode.com/problems/maximum-product-subarray/
"""
def maxProduct(nums):
        
        res = max(nums)
        
        curMin, curMax = 1, 1
        
        for n in nums:
          temp = curMax
          curMax = max (n*curMax, n*curMin, n)
          curMin = min (temp*n, n*curMin, n)
          
          res = max(res, curMax)
          
        return res


print(maxProduct(nums = [2,3,-2,4]))