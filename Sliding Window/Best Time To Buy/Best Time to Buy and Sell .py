#maximize the profit, figuring out best time to buy (lowest) and sell (highest) with respect to time (order matters)
def buySell(slist):
    l, r = 0,1 #initialize for buy and sell
    mprofit = 0 #max profit

    #while right pointer reaches the end
    while r < len(slist):

        #we check with previous time and current time if they are in ascending order
        #then compute new profit
        if slist[l] < slist[r]:
            cprofit = slist[r] - slist[l]
            # compare it with previous profit
            mprofit = max(cprofit, mprofit)

        else:
            #we move left pointer further towards right pointer
            l = r
            
        r+=1
    return mprofit

print(buySell([7,1,5,3,6,4]))
print(buySell([7,6,4,3,1]))