"""
https://leetcode.com/problems/binary-tree-maximum-path-sum
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ## to change while we recursively access it
        res = [root.val]
        
        def dfs(root):
          if not root:
            return 0
          
          
          ## to traverse the left and right half
          leftMax = dfs(root.left)
          rightMax = dfs(root.right)
          
          
          ## this is to ensure we avoid negative values
          leftMax = max(leftMax, 0)
          rightMax = max(rightMax, 0)
          
          
          ## this is to keep track of max result either the current path or the split path would
          ## be the max resulting value
          res[0] = max(res[0], root.val+leftMax+rightMax)
          
          ## we return the path max either left or right
          return root.val + max(leftMax, rightMax)
        
        
        dfs(root)
        
        return res[0]