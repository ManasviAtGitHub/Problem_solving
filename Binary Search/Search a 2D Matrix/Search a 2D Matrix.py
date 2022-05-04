"""
Problem statement is return True 
if a number exists in the matrix

matrix has some properties
is strictly in increasing order 
from first row,col to first row last col and last row first col

Use double binary search to first locate row where to find the target number
and then search in that row to check if the number exists
"""

def searchMatrix(matrix, target):

    row, col = len(matrix), len(matrix[0])

    top, bottom = 0, row-1
    v_mid = 0
    while top<=bottom:
        v_mid = (top + bottom) // 2

        if target > matrix[v_mid][-1]:
            top = v_mid + 1
        elif target < matrix[v_mid][0]:
            bottom = v_mid - 1
        else:
            break
    
    if top > bottom :
        return False
    
    l, r = 0, col -1
    while l<=r:
        h_mid = (l+r)//2
        if target > matrix[v_mid][h_mid]:
            l = h_mid + 1
        elif target < matrix[v_mid][h_mid]:
            r = h_mid - 1
        else:
            return True

    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))