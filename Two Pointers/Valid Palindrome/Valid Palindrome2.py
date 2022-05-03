
#with better space complexity
def validPalindrome(s):
    # let's use two pointer approach
    left, right =0, len(s)-1
    while left<right:
        while left<right and not s[left].isalnum():
            left += 1
        while right>left and not s[right].isalnum():
            right -= 1
    
        if s[left].lower() != s[right].lower():
            return False
    
        left, right = left+1, right-1
    return True

print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("race a car"))


    