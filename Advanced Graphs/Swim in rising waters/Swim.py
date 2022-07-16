
"""
https://leetcode.com/problems/swim-in-rising-water
"""
import heapq

def swimInWater(grid):
      N = len(grid)
      
      visit = set()
      
      minH = [[grid[0][0], 0, 0]]
      
      directions = [[0,1],[0,-1],[1,0],[-1,0]]
      
      visit.add((0,0))
      
      while minH:
        t, r, c = heapq.heappop(minH)
        
        if r == N-1 and c == N-1:
          return t
        for dr, dc in directions:
          neiR, neiC = r+dr, c+dc
          if(neiR<0 or neiC<0 or 
             neiR==N or neiC==N or
             (neiR, neiC) in visit):
            continue
          
          visit.add((neiR, neiC))
          
          heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])


print(swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))