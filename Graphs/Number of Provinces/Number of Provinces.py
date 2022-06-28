"""
https://leetcode.com/problems/number-of-provinces
"""

def findCircleNum(isConnected) -> int:
      
      ## list for keeping track of individual parent and ranks
      
      n = len(isConnected)
      par = [i for i in range(n)]
      
      rank = [1] * n

      def find(n1):
        res = n1

        while res != par[res]:
            par[res] = par[par[res]]
            res = par[res] 
        return res
    
      def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return 0
        if rank[p2] > rank[p1]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            par[p2] = p1
            rank[p1] += rank[p2]
        return 1
    
      res = n
      
      for i in range(n):
        for j in range(i+1, len(isConnected[0])):
          if isConnected[i][j] != 0:
            res-=union(i, j)
            
          
      return res


print(findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))