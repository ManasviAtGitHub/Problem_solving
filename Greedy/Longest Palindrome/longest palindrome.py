
"""
https://leetcode.com/problems/longest-palindrome
"""

def longestPalindrome(s):
      
      mapletters = {}
      
      pal = 0
      one = False
      
      if len(s) <= 1:
        return 1
      
      
      for letter in s:        
        mapletters[letter] = 1 + mapletters.get(letter, 0)
        
        
        
      for letter in s:
        if mapletters[letter]%2==0:
          pal+=mapletters[letter]
          mapletters[letter] = 0
          
        
        elif one == False and mapletters[letter]==1:
          one = True
          pal+=1
          mapletters[letter] = 0
          
        elif mapletters[letter]!=1 and mapletters[letter]%2 == 1:
          pal = pal + (mapletters[letter] - 1)
          mapletters[letter] = 1
      
      
      return pal


print(longestPalindrome("abccccdd"))
print(longestPalindrome("ccc"))