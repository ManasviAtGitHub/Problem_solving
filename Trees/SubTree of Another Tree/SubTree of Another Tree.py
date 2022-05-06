def isSameTree(self, p, q):
        if not p and not q:
            return True
            
        if (p and q) and (p.val == q.val):
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
            
        return False
    
    
    
def isSubtree(self, root, subRoot):
        
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))