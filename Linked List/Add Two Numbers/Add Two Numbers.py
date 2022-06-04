"""
https://leetcode.com/problems/add-two-numbers/
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        
        #Both list should be null  and carry 0, then we stop iterating
        while l1 or l2 or carry:
          val1 = l1.val if l1 else 0
          val2 = l2.val if l2 else 0
          
          val = val1 + val2 + carry
          
          carry = 1 if val1+val2 > 9 else 0
          val = val%10
          cur.next = ListNode(val)
          cur = cur.next
          
          l1 = l1.next if l1 else None
          l2 = l2.next if l2 else None
        
        return dummy.next