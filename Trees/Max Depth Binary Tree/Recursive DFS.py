def maxDepth(self, root):
    """ https://leetcode.com/problems/maximum-depth-of-binary-tree/"""
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))