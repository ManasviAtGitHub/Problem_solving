from regex import P


def plusOne(digits):
    carry = 1
    
    for d in range(len(digits)-1, -1, -1):

        if carry==1 and digits[d]<9:
            carry = 0
            digits[d]+=1
        else:
            if digits[d]+carry<=9:
                digits[d]+=carry
            else:
                digits[d]=0


    if digits[0]==0:
        addOn = [1]
        # addOn.append(1)
        addOn.extend(digits)
        return addOn

    return digits



        
print(plusOne([9,8,3]))
print(plusOne([9,9,9]))
print(plusOne([1,9,9]))