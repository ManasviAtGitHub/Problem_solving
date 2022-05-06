"""
        we know array is sorted upto a pivot where it is rotated
        
        eg.. [0,1,2,4,5,6,7]
        actual input : [4,5,6,7,0,1,2]
        target = 2
        
        we first partition binary search style
        
        the mid is guranteed to be either 
        be right side of left sorted array 
        or left side of right sorted array
        until we find our target.
        
        using this to our advantage,
        mid = 0 + 6 // 2 = 3
        [mid=3] = 7
        we need to figure where we are left or right side
            so compare [l=0]=4 <= [mid=3]=7 : if true we are at left sorted part
            we check if target is within this left sorted part
                2 > [mid=3]=7 or 2 < [l=0]=4 if true move l beyond mid
                else r should be mid - 1
            
           eg : [4,5,6,-1,0,1,2]
           where l=0 mid =3, if fails as 4<-1 not true we are at right sorted part
           compare 2 < -1 or 2 > 2
        
"""
def search_sorted(nums, target):
    l, r = 0, len(nums) - 1
        
    while l<=r:
        mid = (l+r)//2     
        # [4,5,6,7,0,1,2]
            
        if target == nums[mid]:
            return mid
            
        if nums[l] <= nums[mid]:
            if target < nums[l] or target > nums[mid] :
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
 
    return -1


print(search_sorted([4,5,6,7,0,1,2],0))
print(search_sorted([4,5,6,7,0,1,2],3))