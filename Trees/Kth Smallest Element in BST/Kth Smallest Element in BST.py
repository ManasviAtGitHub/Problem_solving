
"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst
"""

def kthSmallest(root, k) -> int:
        
        
        curr = root
        stack = []
        
        
        while curr or stack:
          while curr:
            stack.append(curr)
            curr = curr.left
          
          curr = stack.pop()
          k-=1
          if k == 0:
            return curr.val
          
          curr = curr.right