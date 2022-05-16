
def permute(nums):
    res = []

    if len(nums) == 1:
        return [nums[:]]
    
    for i in range(len(nums)):
        n = nums.pop(0)
        p_set= permute(nums)

        for p in p_set:
            p.append(n)
        
        res.extend(p_set)
        nums.append(n)
    return res


print(permute(nums = [1,2,3]))
print("\n",permute(nums = [0,1]))

