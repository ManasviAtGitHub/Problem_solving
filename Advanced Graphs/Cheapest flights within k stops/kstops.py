
"""
https://leetcode.com/problems/cheapest-flights-within-k-stops
"""
def findCheapestPrice(n, flights, src, dst, k):
      
      prices = [float("inf")]*n
      
      prices[src] = 0
      
      
      for i in range(k+1):
        tmpPrices = prices.copy()
        
        for s, d, p in flights:
          if prices[s] == float('inf'):
            continue
          
          if prices[s] + p < tmpPrices[d]:
            tmpPrices[d] = prices[s] + p
        
        prices = tmpPrices
      
      
      return -1 if prices[dst] == float("inf") else prices[dst]


print(findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))