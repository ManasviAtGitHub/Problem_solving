def longestSubstring(s):

    # eg. abbcdefbc
    
    chars = set() #will store unique chars
    r, l, result =0, 0, 0

    
    while r<len(s):
        #we check if curr char is already set loop till we remove it ... 
        #in our case 3rd char b .. (a,b), so both had to be removed
        
        while s[r] in chars:
            chars.remove(s[l])
            l+=1
        # add every char to set, previous loop ensures we remove till the duplicate
        chars.add(s[r])

        result = max(result, len(chars))
        # result = max(result, r-l+1)
        r+=1

    return result


print(longestSubstring("abbcdefbc"))
print(longestSubstring("abcabcbb"))


