def twoSum(nums,target):
    #we can use hashmap and do this in one pass
    hMap = {}
    #this is on the basis that solution is guranteed to exist in the list
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hMap:
            return [hMap[diff],i] # returns the indexes as list
        hMap[n] = i
    return


print(twoSum([3,2,4],6))
print(twoSum([2,7,11,15],9))
print(twoSum([3,3],6))