#https://leetcode.com/problems/balanced-binary-tree/
def isBalanced(self, root):
        
        balance = [True]
        
        def dfs(root):
            
            if root is None :
                return balance[0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if (abs(left-right)>1):
                balance[0] = False
                return balance[0]
            
            return max(left,right) + 1
        
        dfs(root)
        
        return balance[0]