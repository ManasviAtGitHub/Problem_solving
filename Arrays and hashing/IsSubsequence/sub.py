
"""
https://leetcode.com/problems/is-subsequence
"""
def isSubsequence(s,t):
      
      
      if s=="":
        return True
      
      if len(s)==1 and len(t)==1:
        if s==t:
          return True
        else:
          return False
      
      k = ""
      i = 0
      for v in t:
        if i < len(s) and s[i] == v:
          k+=s[i]
          i+=1
        
        if k == s:
          return True
        
      
      return False


print(isSubsequence("abc", "ahbgdc"))