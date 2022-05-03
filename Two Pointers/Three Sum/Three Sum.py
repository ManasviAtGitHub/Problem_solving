#return list of three numbers adding up to 0
def threeSum(slist):

    if len(slist) < 3:
        return []
    result =[]

    slist.sort()

    for i, n in enumerate(slist):

        if i>0 and n==slist[i-1]:
            continue

        l, r = i+1, len(slist) - 1
        while l<r:
            sum = n + slist[l] + slist[r]
            if  sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                result.append([n,slist[l], slist[r]])
                l+=1
                while slist[l]==slist[l-1] and l<r:
                    l+=1
    return result


print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([]))
print(threeSum([0]))
print(threeSum([0,0,0]))
