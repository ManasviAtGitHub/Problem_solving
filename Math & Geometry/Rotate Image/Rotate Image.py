
"""
https://leetcode.com/problems/rotate-image
"""
def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose 
        
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
        
        #reflect
        
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1],matrix[i][j]
