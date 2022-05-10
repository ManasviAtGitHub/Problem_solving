"""https://leetcode.com/problems/number-of-1-bits/"""

def hammingWeight(n):
        result = 0
        
        while n:            
            n = n & (n-1)            
            result += 1
        return result

