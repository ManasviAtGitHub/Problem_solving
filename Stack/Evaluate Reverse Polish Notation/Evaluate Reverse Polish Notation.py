from os import stat


def eval(slist):
    stack = []
    for i in slist:
        if i=="+":
            stack.append(stack.pop()+stack.pop())
        elif i=="*":
            stack.append(stack.pop()*stack.pop())
        elif i=="-":
            a, b = stack.pop(), stack.pop()
            stack.append(b-a)
        elif i=="/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(i))
    
    return stack.pop()

print(eval(["2","1","+","3","*"]))
print(eval(["4","13","5","/","+"]))
print(eval(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))