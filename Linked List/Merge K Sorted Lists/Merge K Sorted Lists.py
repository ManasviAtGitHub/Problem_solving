
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):

        # input is list of K sorted lists, we only get head not the list(we can just get that with head.next)
    
        if not lists  or len(lists) == 0:
          return None
        
        #Each round we merge lists and shrink it
        #initially it is of k size , so this will max out in k iterations hence nlogk runtime
        while len(lists)>1:
          mergedLists = []

          #we take first 2 and merge then next 2, and so on
          for i in range(0, len(lists),2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1)<len(lists) else None
            
            mergedLists.append(self.mergelist(l1,l2))

          #this helps to shrink lists
          lists = mergedLists
          
        return lists[0]
      
    
    def mergelist(self, l1, l2):

      dummy = ListNode()
      tail = dummy
      while l1 and l2:
        if l1.val < l2.val:
          tail.next = l1
          l1 = l1.next
        else:
          tail.next = l2
          l2 = l2.next
        
        tail = tail.next
      
      if l1:
        tail.next = l1
      if l2:
        tail.next = l2
      
      
      return dummy.next
    



    # Input: lists = [[1,4,5],[1,3,4],[2,6]]
    # Output: [1,1,2,3,4,4,5,6]   

input = []

node3 = ListNode(5)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
input.append(node1)
node6 = ListNode(4)
node5 = ListNode(3, node6)
node4 = ListNode(1, node5)
input.append(node4)
node8 = ListNode(6)
node7 = ListNode(2, node8)
input.append(node7)
sol = Solution()


l = sol.mergeKLists(input)

while l:
    print(l.val)
    l = l.next

