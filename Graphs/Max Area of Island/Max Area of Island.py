
"""
https://leetcode.com/problems/max-area-of-island/

"""
def maxAreaOfIsland(grid):
        count=0
        max_size=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count+=1
                    max_size = max(max_size,callBFS(grid,i,j))
        return max_size
    
def callBFS(grid,i,j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]==0:
            return 0
        grid[i][j] = 0
        curr = 1

        s = callBFS(grid,i+1,j)
        n = callBFS(grid,i-1,j)
        e = callBFS(grid,i,j+1)
        w = callBFS(grid,i,j-1)

        return max (1,curr+s+n+e+w)


print(maxAreaOfIsland(grid = 
[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
))

print(maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))