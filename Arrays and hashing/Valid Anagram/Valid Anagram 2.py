
def validAnagram(s, t):
    return sorted(s) == sorted(t)

    
#not memory efficient though
def validAnagram_c(s:str, t:str):
    
    if len(s)!=len(t):
        #simply strings have different lengths so cannot be anagram
        return False
    
    s= list(s)

    for i in t:
        try :
            if s.remove(i):
                continue
        except:
            return False


    return True
    



print(validAnagram("GAME","MAGE"))
print(validAnagram("GAMER","IMAGE"))

print(validAnagram_c("GAME","MAGE"))
print(validAnagram_c("GAMER","IMAGE"))

