class Solution:
    def numIslands(self, grid):
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count+=1
                    self.callBFS(grid,i,j)
        return count
    
    def callBFS(self,grid,i,j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]=="0":
            return
        grid[i][j] = "0"
        self.callBFS(grid,i+1,j)
        self.callBFS(grid,i-1,j)
        self.callBFS(grid,i,j+1)
        self.callBFS(grid,i,j-1)

call = Solution()
print(call.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]))