def hammingWeight(n):
        result = 0
        
        while n:
            
            result += n%2
            n = n>>1
            
        return result