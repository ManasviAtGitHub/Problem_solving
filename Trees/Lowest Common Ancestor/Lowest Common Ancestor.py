
"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""
def lowestCommonAncestor(self, root, p, q):
        
        if not root :
            return False
        
        
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
                
            elif p.val < root.val and q.val < root.val:
                root = root.left
            
            else :
                return root