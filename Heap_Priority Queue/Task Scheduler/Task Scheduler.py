"""
https://leetcode.com/problems/task-scheduler
"""

import heapq
from collections import deque
from collections import Counter


def leastInterval(tasks, n) -> int:

    ##hashmap for every character count
        count = Counter(tasks)
    ##we make count negative as minheap is used
        maxHeap = [-cnt for cnt in count.values()]
    
    ##heapify to convert the map into maxheap
        heapq.heapify(maxHeap)
    
    #for every iteration we tic the time counter
        time = 0
    
    #queue for waiting time of character before
    #assigning back to maxheap
        q = deque()
    
        while maxHeap or q:
          time += 1
        
          if maxHeap:
            # here we ensure to reduce the character count since it was negative
            # we add 1 to reduce
            count = 1+heapq.heappop(maxHeap)

            #if count is greater than 0, we add it in the queue
            if count:
              q.append([count, time + n])
          
          #we check if the current character has waited for n + time alloted
          #if yes we push it back to maxheap, this gurantees we never push 0 
          #as it was entered in the queue only if count > 0
          if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])
          
        # return total time taken to complete all task
        return time
    

print(leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))


