"""
https://leetcode.com/problems/min-cost-to-connect-all-points
"""

import heapq
def minCostConnectPoints(points):
        N = len(points)
        adj = {i:[] for i in range(N)}
        
        for i in range(N):
          x1, y1 = points[i]
          for j in range(i+1, N):
            x2, y2 = points[j]
            dist = abs(x1-x2) + abs(y1-y2)
            adj[i].append([dist,j])
            adj[j].append([dist,i])
          
          
       
        res = 0
        visit = set()
        minHeap = [[0,0]]
        
        while len(visit)<N:

          cost, i = heapq.heappop(minHeap)
          if i in visit :
            continue

          res+=cost
          visit.add(i)
          
          for neighborCost, neighbor in adj[i]:
            if neighbor not in visit:
              heapq.heappush(minHeap, [neighborCost, neighbor])


        return res


print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))