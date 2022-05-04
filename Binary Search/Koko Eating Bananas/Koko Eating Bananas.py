
"""
https://leetcode.com/problems/koko-eating-bananas/
"""
def findMinSpeed(piles, h):

    l, r = 1, max(piles)
    k = 0
    while l<=r:
        m = (l+r)//2
        time = 0

        for p in piles:
            #the edge case where we have to eat largest pile each hour
            #requires the below formula
            time+=((p-1)//m) + 1

        if time <= h:
            k = m
            r = m - 1
        else :
            l = m + 1

    return k


print(findMinSpeed([3,6,7,11], h = 8))
print(findMinSpeed([30,11,23,4,20], h = 5))
print(findMinSpeed([30,11,23,4,20], h = 6))
print(findMinSpeed([312884470],968709470))