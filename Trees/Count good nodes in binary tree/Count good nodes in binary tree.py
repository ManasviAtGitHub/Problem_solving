
"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree
"""
def goodNodes(self, root):
        
        def dfs(node, maxVal):
          if not node:
            return 0
          
          res = 1 if node.val >= maxVal else 0
          
          maxVal = max(maxVal, node.val)
          
          res+=dfs(node.left, maxVal)
          res+=dfs(node.right, maxVal)
          
          return res
        
        return dfs(root, root.val)