def maxSubArray(nums):
        
        sum=0
        largest=-2147483647
        for val in nums:
            
            # sum+=val
            
            sum = max(sum+val,val)
            
            largest = max(largest, sum)
            
            
        return largest

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([4,-1,2,1]))
print(maxSubArray([-2]))