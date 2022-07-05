
"""
https://leetcode.com/problems/hand-of-straights
"""
import heapq

def isNStraightHand(hand, groupSize):
        
        if len(hand) % groupSize:
          return False
        
        count = {}
        
        for n in hand:
          count[n] = 1 + count.get(n, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)
        
        while minH:
          
          first = minH[0]
          
          for i in range(first, first + groupSize):
            if i not in count:
              return False
            
            count[i] -= 1
            
            if count[i] == 0:
              if i!=minH[0]:
                return False
              
              heapq.heappop(minH)
        
        return True

print(isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))