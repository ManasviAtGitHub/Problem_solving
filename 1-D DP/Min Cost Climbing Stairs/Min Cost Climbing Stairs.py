"""
https://leetcode.com/problems/min-cost-climbing-stairs/
"""

def minCostClimbingStairs(cost):
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
            
        return min(cost[0], cost[1])

print(minCostClimbingStairs([10,15,20]))
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))