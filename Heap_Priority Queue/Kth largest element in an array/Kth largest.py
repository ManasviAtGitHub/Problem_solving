def findKthLargest(nums,k):
        
        nums.sort()
        return nums[len(nums) - k]


print(findKthLargest([1,5,6,4,3,2],2))