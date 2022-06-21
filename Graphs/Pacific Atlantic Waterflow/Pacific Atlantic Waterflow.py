"""
https://leetcode.com/problems/pacific-atlantic-water-flow
"""


def pacificAtlantic(heights):
        ROWS, COLS =len(heights), len(heights[0])
        
        pacific, atlantic = set(), set()
        
        def dfs(r, c, visit, prevHeight):
          if((r,c) in visit or r<0 or 
             c<0 or r==ROWS or c==COLS or
             heights[r][c] < prevHeight):
            return
          
          visit.add((r,c))
          dfs(r+1, c, visit, heights[r][c])
          dfs(r-1, c, visit, heights[r][c])
          dfs(r, c+1, visit, heights[r][c])
          dfs(r, c-1, visit, heights[r][c])
        
        
        for c in range(COLS):
          dfs(0, c, pacific, heights[0][c])
          dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        
        for r in range(ROWS):
          dfs(r, 0, pacific, heights[r][0])
          dfs(r,COLS-1, atlantic, heights[r][COLS-1])
        
        
        return pacific.intersection(atlantic)
        
#         res = []
#         for r in range(ROWS):
#           for c in range(COLS):
#             if (r,c) in pacific and (r,c) in atlantic:
#               res.append([r,c])
#         return res



print(pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))