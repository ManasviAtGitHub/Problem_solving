import heapq
def kClosest(points, k):
        minHeap = []
        for x,y in points:
            dist = (abs(x)**2) + (abs(y)**2)
            minHeap.append([dist, x, y])
            
        
        heapq.heapify(minHeap)
        r = []
        
        while k>0:
            dist, x, y = heapq.heappop(minHeap)
            r.append([x,y])
            k-=1
        
        return r


print(kClosest(points = [[1,3],[-2,2]], k = 1))