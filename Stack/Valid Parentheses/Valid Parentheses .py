def validParentheses(s):
    stack =[]
    # we map closing parentheses 
    # this ensures if start with closing parentheses then return False

    closeToOpen = {")" : "(", "]" : "[", "}":"{"}

    for c in s:
        # matches c with keys in the map
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        
        else:
            stack.append(c)
        
    return True if not stack else False


print(validParentheses("}{[])"))
print(validParentheses("[{()}]"))
print(validParentheses("((()))"))

