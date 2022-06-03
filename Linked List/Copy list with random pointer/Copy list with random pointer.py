
"""
https://leetcode.com/problems/copy-list-with-random-pointer
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
      
      #this is useful when the node is pointing to null value
      #we utilize the face in final loop
      oldToNew= {None : None}
      
      cur = head
      
      #deep copying nodes to hashmap with their values
      #we can't save it any order hence use hashmap
      while cur:
        copy = Node(cur.val)
        oldToNew[cur] = copy
        cur = cur.next
      
      cur = head
      
      #now for each node we lookup hashmap to find respective pointers
      
      while cur:
        copy = oldToNew[cur]
        copy.next = oldToNew[cur.next]
        copy.random = oldToNew[cur.random]
        cur = cur.next
      
      return oldToNew[head]