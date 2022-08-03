"""
https://leetcode.com/problems/set-matrix-zeroes
"""

def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        
        row = []
        col = []
        
        for r in range(ROWS):
          for c in range(COLS):
            
            if matrix[r][c] == 0:
              row.append(r)
              col.append(c)
        
        for i in row:
          for j in range(COLS):
            if matrix[i][j]!=0:
              matrix[i][j] = 0
            
            
        for i in col:
          for j in range(ROWS):
            if matrix[j][i]!=0:
              matrix[j][i] = 0