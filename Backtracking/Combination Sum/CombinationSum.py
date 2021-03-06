"""
https://leetcode.com/problems/combination-sum/
"""

def combinationSum(candidates, target):
        result = []
        
        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if i>= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i,curr, total+candidates[i])
            
            curr.pop()
            dfs(i+1,curr, total)
        
        dfs(0,[],0)
        
        return result

print(combinationSum([1,2],3))