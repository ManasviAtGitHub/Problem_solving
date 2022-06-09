
"""
https://leetcode.com/problems/binary-tree-level-order-traversal
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root):
        
      res = []
      
      q = Collection.deque()
      if root :
        q.append(root)
      
      while q:
        qlen = len(q)
        
        level = []
        for i in range(qlen):
          node = q.popleft()
          level.append(node.val)
          
          if node.left : 
            q.append(node.left)
          if node.right : 
            q.append(node.right)
        
        res.append(level)
            
      return res