def isHappy(n):
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = sumOfSquares(n)
            
            if n == 1:
                return True
            
        
        return False
            
        
def sumOfSquares(n):
        res = 0
        
        while n:
            d = n%10
            d = d**2
            res +=d
            n = n//10
        
        return res


print(isHappy(19))
print(isHappy(2))