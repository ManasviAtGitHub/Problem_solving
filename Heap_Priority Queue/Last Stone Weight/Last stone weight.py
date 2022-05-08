import heapq
"""
https://leetcode.com/problems/last-stone-weight/
"""
def lastStone(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        # don't need to check for equal values as popping does the job
        if second > first:
            heapq.heappush(stones, first - second)
    
    # append 0 if no element is their then will return 0
    stones.append(0)
    return abs(stones[0])
    



print(lastStone(stones = [2,7,4,1,8,1]))