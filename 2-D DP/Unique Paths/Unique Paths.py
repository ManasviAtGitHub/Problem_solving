"""
https://leetcode.com/problems/unique-paths/
"""

def uniquePaths(m,n):
    row = [1]*n

    # as last row and colunns are always we use
    # that fact to our advantage
    for i in range(m-1):
        newRow = [1]*n
        
        for j in range(n-2, -1, -1):
            newRow[j] = newRow[j+1] + row[j]
        
        row = newRow

    return row[0]

print(uniquePaths(3,7))