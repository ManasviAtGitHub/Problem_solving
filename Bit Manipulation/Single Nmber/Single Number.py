"""
https://leetcode.com/problems/single-number/
"""
def singleNumber(nums):
        result = 0
        for n in nums:
            result = result ^ n
        
        return result

print(singleNumber([4,2,1,2,1]))