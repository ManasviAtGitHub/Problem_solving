  
"""
https://leetcode.com/problems/sum-of-two-integers
"""

def getSum(a, b):
      
      def add(a,b):
        if not a or not b:
          return a or b
        
        return add(a^b, (a&b)<<1)
      
      
      
      if a*b < 0:
        
        if a>0:
          return getSum(b,a)
        
        if add(~a, 1) == b:
          return 0
        
        if add(~a, 1) < b:
          return add(~add(add(~a,1), add(~b,1)), 1)
      
      return add(a,b)


print(getSum(-1,1));