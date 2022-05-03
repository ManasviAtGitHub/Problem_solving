
#problem may contain characters other than alpha numeric, so that has to be taken in account 
def validPalindrome(s):
    n =""
    for c in s:
        #check if alpha numeric
        if c.isalnum():
            #add to string in lower case
            n+=c.lower()
    #check if reverse is same as original
    return n == n[::-1]


print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("race a car"))

