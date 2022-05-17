def robHouses(nums):
        rob1, rob2 = 0, 0
      
        for n in nums:
            temp = max(n+rob1, rob2)    
            rob1 = rob2
            rob2 = temp
        
        return rob2
    
def rob(nums):
        
        if len(nums)==1:
            return nums[0]
        
        return max(robHouses(nums[:-1]), robHouses(nums[1:]))


print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))