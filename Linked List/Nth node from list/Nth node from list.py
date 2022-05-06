"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(self, head, n):
        
        dummy = ListNode(0,head)
        left = dummy
        right = head
        
        while n>0 and right:
            right = right.next
            n-=1
        
        while right:
            left = left.next
            right = right.next
            
        
        left.next = left.next.next
        
        return dummy.next