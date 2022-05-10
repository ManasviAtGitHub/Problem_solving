def subsets(nums):
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            # print(f"bitmask of {i} : {bitmask}")
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
            # print(f"Output {output}")
        
        return output

print(subsets([1,2,3]))