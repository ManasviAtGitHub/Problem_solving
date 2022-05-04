
"""
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""

"""
    We take 2 queues (deque)
    indexQ, valQ
    for each num in list
        check if valQ.isEmpty and num > valQ_last_element
        as the valQ is monotonically decreasing*
            if true then pop last element from valQ and
            corresponding index in indexQ
        if false we continue to append val and index

        check if curr_index - start_of_indexQ + 1 > k
            if true remove start elements of both queues
        if false we continue
        then check curr_index + 1 >= k
            then append the start_valQ to result
"""

from collections import deque


def slidingWindowMaximum(nums,k):
    
    indexQ = deque()
    valueQ = deque()
    result = []
    for i, n in enumerate(nums):
        #Maintain a decreasing value deque
        while valueQ and n > valueQ[-1]:
            #we remove all elements if found a larger one
            valueQ.pop()
            indexQ.pop()
        #continue to add elements in both queues
        valueQ.append(n)
        indexQ.append(i)

        # handling the edge case when you have more smaller values than
        # the window of k

        if i - indexQ[0] + 1 > k :
            # as the largest element is no longer in the window
            # so we remove it from left (since decreasing queue)
            valueQ.popleft()
            indexQ.popleft()
        
        # start adding to result when window size is reached
        if i + 1>=k:
            result.append(valueQ[0])
        
    return result




print(slidingWindowMaximum([1,3,-1,-3,5,3,6,7],3))