
"""
https://leetcode.com/problems/palindromic-substrings
"""


def countSubstrings(s):
        
        def countPalindrome(s,l,r):
          res = 0
          while l>=0 and r<len(s) and s[l] == s[r]:
            res+=1
            l-=1
            r+=1
          
          return res
        
        final = 0
        
        for i in range(len(s)):
          ## for all odd palindromes
          final+=countPalindrome(s, i, i)
          
          ## for even palindromes
          final+=countPalindrome(s, i, i+1)
        
        
        return final


print(countSubstrings("abc"))