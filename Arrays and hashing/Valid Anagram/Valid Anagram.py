def validAnagram(s, t):

    if len(s)!=len(t):
        #simply strings have different lengths so cannot be anagram
        return False;
    
    S, T = {},{}

    for i in range(len(s)):
        #store each character as key
        #and its value as repeatation count
        S[s[i]] = 1 + S.get(s[i], 0)
        T[t[i]] = 1 + T.get(t[i], 0)
    
    for key in S:
        #now just check if for any key it returns different value count and thats it
        if S[key]!=T.get(key,0):
            return False
        
    return True


print(validAnagram("GAME","MAGE"))
print(validAnagram("GAMER","IMAGE"))
