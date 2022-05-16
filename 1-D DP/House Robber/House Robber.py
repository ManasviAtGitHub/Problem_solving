"""
https://leetcode.com/problems/house-robber/

Consider [2,7,9,3,1]

At each iteration consider, max till that point...
how max is computed its either prev, or prev-1 + curr
[2] => 2
[2,7] => 2,7
[2,7,9] => 2 7 2+9=11
[2,7,9,3] => 2 7 11 7+3=10
[2,7,9,3,1] => 2 7 11 11 11+1=12
return 12
At any given point we only need previous 2 values only
"""

def rob(nums):
    rob1, rob2 = 0, 0
    for n in nums:
        temp = max(n+rob1, rob2)    
        rob1 = rob2
        rob2 = temp
            
    return rob2


print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))

