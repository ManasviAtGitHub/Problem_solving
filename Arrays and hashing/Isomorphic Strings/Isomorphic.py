"""
https://leetcode.com/problems/isomorphic-strings
"""



def isIsomorphic(s,t):
        
        
        if len(s)!=len(t):
          return False
        
        if s==t:
          return True
        s_map = {}
        t_map = {}
        res1 =""
        res2 =""
        
        
        for i in range(len(s)):
          s_map[t[i]] = s[i]
          t_map[s[i]] = t[i]
          
        for i in range(len(s)):
          res1+=t_map[s[i]]
          res2+=s_map[t[i]]
        
        if res1== t and res2==s:
          return True
        
        return False


print(isIsomorphic("paper", "title"))
print(isIsomorphic("foo", "bar"))