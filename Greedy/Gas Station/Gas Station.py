
"""
https://leetcode.com/problems/gas-station/
"""

def canCompleteCircuit(gas,cost):
      
           
      if sum(gas) < sum(cost):
        return -1

      total = 0
      res = 0
      
      for i in range(len(gas)):
        total+=(gas[i] - cost[i])
        
        if total < 0:
          total = 0
          res = i + 1
        
      
      return res


print(canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1]))
print(canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
print(canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))

