
"""
https://leetcode.com/problems/reverse-nodes-in-k-group
"""
def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      
      dummy = ListNode(0, head)
      groupPrev = dummy
      
      
      def getKth(curr, k) :
        while curr and k>0:
          curr = curr.next
          k -= 1
        return curr
      
      while True:
        
        kth = getKth(groupPrev, k)
        
        if not kth:
          break
        
        groupNext = kth.next
        
        prev, curr = kth.next, groupPrev.next
        
        while curr != groupNext:
          tmp = curr.next
          curr.next = prev
          prev = curr
          curr = tmp
          
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
      
      return dummy.next