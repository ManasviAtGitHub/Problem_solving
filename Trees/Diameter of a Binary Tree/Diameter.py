
"""https://leetcode.com/problems/diameter-of-binary-tree/"""
def diameterOfBinaryTree(self, root):
        diameter = [0]
            
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
                
            diameter[0] = max(diameter[0], left + right)
                
            return max(left,right) + 1
            
        
        dfs(root)
        return diameter[0]
