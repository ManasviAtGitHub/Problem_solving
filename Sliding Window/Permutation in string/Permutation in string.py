"""https://leetcode.com/problems/permutation-in-string"""

def checkInclusion(s1, s2):
      if len(s1) > len(s2) : return False
      
      s1_c, s2_c= [0] * 26, [0] * 26
      
      #initializing window of size s1
      for i in range(len(s1)):
        s1_c[ord(s1[i]) - ord('a')] +=1
        s2_c[ord(s2[i]) - ord('a')] +=1
      
      #remember we are looking for 26 matches
      matches = 0
      
      for i in range(26):
        matches+=(1 if s1_c[i] == s2_c[i] else 0)
      
      
      left = 0
      
      for right in range(len(s1), len(s2)):
        
        if matches == 26 : return True
        
        i_next = ord(s2[right]) - ord('a')
        
        prev = ord(s2[left]) - ord('a')
        
        

        # we obtain the previous character index in array
        # now two cases are possible
        # if they both are equal now 
        # we increment matches, counter of matching character (this is further adjusted in the next case)
        # it will be generally the case when we have no matching previous character
        # else the it actually matched previously so we decrement from string 1 and check it
        # this time decrementing matches (this will be the case when we have a matching previous character)

        s2_c[prev]-=1
        
        if s1_c[prev] == s2_c[prev]:
          matches +=1
        elif s2_c[prev] == s1_c[prev] - 1:
          matches -=1
        
        

        # this is to check whether current character matches, so we increment matches
        # it only happens if both strings has that character
        # or else we just check to balance out the matches counter
        
        s2_c[i_next]+=1
        
        
        if s2_c[i_next] == s1_c[i_next]:
          matches +=1
        elif s1_c[i_next]+1 == s2_c[i_next]:
          matches-=1
        
        
        
        left+=1
        
      
      return matches == 26




print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))

print(checkInclusion(s1 = "ab", s2 = "eidboaoo"))