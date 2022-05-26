def spiralOrder(matrix):
      
      res = []
      left, right = 0, len(matrix[0])
      top, bottom = 0, len(matrix)
      
      
      #continue till we overlap any 2 of the 4 pointers
      
      while left<right and top<bottom:
        
        # we move from top left to top right
        
        for i in range(left, right):
          res.append(matrix[top][i])
        top+=1 # increment top as next row becomes top boundary
        
        
        #we move from top right to bottom right
        for i in range(top, bottom):
          res.append(matrix[i][right-1])
        right-=1 # decrement right as previous column becomes the new right boundary
        
        
        #consider a vector to understand this better, n x 1,
        #you can't move further without checking overlaps
        if not (left<right and top<bottom):
          break
        
        
        #we move from bottom right to bottom left 
        for i in range(right-1, left-1, -1):
          res.append(matrix[bottom -1][i])
        bottom-=1 #decrement bottom as previous row becomes bottom boundary
        
        #we move from bottom left to top left
        for i in range(bottom-1, top-1, -1):
          res.append(matrix[i][left])
        left+=1 # increment left as next column will be the left boundary
      
      return res



print(spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))