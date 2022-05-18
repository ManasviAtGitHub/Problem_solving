import heapq
def findKthLargest(nums,k):
        nums = [-n for n in nums]
        print(nums)
        l=0
        while k:
            heapq.heapify(nums)
            l = heapq.heappop(nums)
            k-=1
        
        return abs(l)

print(findKthLargest([1,5,6,4,3,2],2))
          
    
