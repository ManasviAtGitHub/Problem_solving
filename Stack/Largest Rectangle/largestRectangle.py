"""
https://leetcode.com/problems/largest-rectangle-in-histogram
"""

def largestRectangleArea(heights) -> int:
      
      maxArea = 0
      
      stack = []
      
      for i, h in enumerate(heights):
        start = i
        
        while stack and stack[-1][1] > h:
          index, height = stack.pop()
          maxArea = max(maxArea, height * (i - index))
          start = index
        
        stack.append((start, h))
        
      for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
      
      return maxArea

print(largestRectangleArea(heights = [2,1,5,6,2,3]))