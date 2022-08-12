
"""
https://leetcode.com/problems/linked-list-cycle-ii
"""

def detectCycle(head):
      

      dummy, slow, fast = head, head, head
      
      while fast and fast.next:
        
        fast = fast.next.next
        
        slow = slow.next
        
        if fast == None:
          return None
        
        if slow == fast:
          while dummy != slow:
            dummy = dummy.next
            slow = slow.next
          return slow
        
      
      return None