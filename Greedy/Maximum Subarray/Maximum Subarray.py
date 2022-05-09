def maxSubArray(nums):
    maxSum = nums[0]
    currSum = 0

    for n in nums:
        if currSum < 0:
            currSum = 0
        currSum +=n
        maxSum = max(maxSum, currSum)
    
    return maxSum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([4,-1,2,1]))
print(maxSubArray([-2]))