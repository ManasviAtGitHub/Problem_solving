"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

def buildTree(preorder, inorder):
      if not preorder or not inorder:
        return None
      # we start with initial element as root
      root = TreeNode(preorder[0])
        
      #the left of this is left part of root and the remains are right
      mid = inorder.index(preorder[0])
        
      ## recursively find the left half
      ## here we pass left of root elements from preorder and inorder lists
      root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
      ## same for right
      root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
      return root