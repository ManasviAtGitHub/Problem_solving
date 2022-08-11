
"""
https://leetcode.com/problems/middle-of-the-linked-list
"""

def middleNode(head):
        
        fast = slow = head
        
        
        
        
        while fast:
          
          if fast.next == None:
            break
            
          fast = fast.next.next
          
          slow = slow.next
          
        
        
        return slow