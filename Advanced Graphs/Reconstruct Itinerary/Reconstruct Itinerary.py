
"""
https://leetcode.com/problems/reconstruct-itinerary/

"""

import collections

def findItinerary(tickets):
        
        adj = {u:collections.deque() for u,v in tickets}
        res = ["JFK"]
        tickets.sort()
        
        for u,v in tickets:
            adj[u].append(v)
        
        def dfs(curr):
            if len(res) ==len(tickets)+1:
                return True
            
            if curr not in adj:
                return False
            
            temp = list(adj[curr])
            
            for v in temp:
                adj[curr].popleft()
                res.append(v)
                
                if dfs(v):
                    return res
                
                res.pop()
                
                adj[curr].append(v)
            
            return False
        dfs("JFK")
        return res



print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
