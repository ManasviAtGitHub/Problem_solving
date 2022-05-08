"""
https://leetcode.com/problems/climbing-stairs/
"""
def stairs(n):

    if n==0:
        return 0
    step1, step2 = 1, 1

    for i in range(n-1):
        temp = step1
        step1 = step1 + step2
        step2 = temp

    return step1


print(stairs(5))