

import collections
import heapq

def networkDelayTime(times, n, k):
      
      edges = collections.defaultdict(list)
      
      for u, v, w in times:
        edges[u].append((v,w))
        
      
      minHeap = [(0,k)]
      
      visit = set()
      
      t = 0
      
      while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        
        if n1 in visit:
          continue
        visit.add(n1)
        t = max(t, w1)
        
        for n2, w2 in edges[n1]:
          if n2 not in visit:
            heapq.heappush(minHeap, (w1+w2, n2))
        
      
      return t if len(visit) == n else -1

print(networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))