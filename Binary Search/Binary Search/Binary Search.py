def binarySearch(nums,target):
    l = 0
    r = len(nums) - 1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid]< target:
            l = mid + 1
        else:
            return mid

    return -1


print(binarySearch([1,2,6,7,8,9],9))