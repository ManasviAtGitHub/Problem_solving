def invertTree(self, root):
        #https://leetcode.com/problems/invert-binary-tree/submissions/
        if not root:
            return None
    
       
        root.right, root.left = root.left, root.right
      
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root