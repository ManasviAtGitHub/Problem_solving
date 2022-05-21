"""
https://leetcode.com/problems/generate-parentheses/
"""

def generateParenthesis(n):
      """
        we open bracket till n,
        but closing can be done only till open
      
      """
      stack = []
      res = []
      
      def generate(op, cl):
        
        if op == cl == n:
          res.append("".join(stack))
          return
        
        if op < n:
          stack.append("(")
          generate(op+1,cl)
          stack.pop()
        
        if cl < op:
          stack.append(")")
          generate(op,cl+1)
          stack.pop()          
        
      generate(0,0)
        
      return res



print(generateParenthesis(3))