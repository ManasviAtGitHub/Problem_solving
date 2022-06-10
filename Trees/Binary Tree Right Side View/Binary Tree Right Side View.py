
"""
https://leetcode.com/problems/binary-tree-right-side-view/
"""
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        
        res = []
        
        q = collections.deque([root])
        
        while q:
          
          qlen = len(q)
          
          rightnode = None
          
          for _ in range(qlen):
            
            node = q.popleft()
            if node:
              rightnode = node
              q.append(node.left)
              q.append(node.right)
          
          if rightnode:
            res.append(rightnode.val)
          
        
        return res

"""
        1
     /     \ 
    2       3
    \        \ 
     5        7
"""






node4 = TreeNode(7)
node3 = TreeNode(5)
# node2 = TreeNode(3)
node2 = TreeNode(3, right=node4) 
node1 = TreeNode(2, right= node3)
root = TreeNode(1,node1, node2)

s = Solution()
print(s.rightSideView(root))