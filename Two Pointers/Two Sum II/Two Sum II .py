def twoSumSorted(slist,target):
    l,r = 0, len(slist) - 1
    
    #doesn't matter as there is a guranteed solution
    while l<r:
        sum = slist[l] + slist[r]

        #shift right pointer to left
        if sum>target:
            r -=1
        #shift left pointer to right
        elif sum<target:
            l +=1
        else:
            return [l, r]


print(twoSumSorted([2,7,11,15], target = 9))
print(twoSumSorted([2,3,4], target = 6))
print(twoSumSorted([-1,0], target = -1))
        
