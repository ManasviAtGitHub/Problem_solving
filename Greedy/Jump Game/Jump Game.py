def canJump(nums):
        
        goal = len(nums)-1 #end
        
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
                
                
        
        return goal==0


print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))