def subsets(nums):
    n = len(nums)
    res =[[]]
    i = 0
    for n in nums:

        gen = [curr + [n] for curr in res]
        # print(gen)
        res+=gen
        # print(res)
    return res

print(subsets([1,2,3]))