
"""
https://leetcode.com/problems/redundant-connection/
"""

def findRedundantConnection(edges):
        
        # here i=0 is going to be useless
        parent = [i for i in range(len(edges) + 1)]
        
        rank = [1] * (len(edges)+1)
        
        
        ## finding the parent of current node
        def findParent(n):
          p = parent[n]
          
          
          while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]
          return p
        
        def union(n1,n2):
          p1, p2 = findParent(n1), findParent(n2)
          if p1 == p2:
            return False
          
          if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]
          
          else:
            parent[p1] = p2
            rank[p2] += rank[p1]
          
          return True
        
        for n1, n2 in edges:
          if not union(n1,n2):
            return [n1, n2]



print(findRedundantConnection(edges = [[1,2],[1,3],[2,3]]))

print(findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))