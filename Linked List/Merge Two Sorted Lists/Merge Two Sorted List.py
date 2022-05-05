from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def merge(self, l1,l2):
        temp = ListNode()
        tail = temp

        #when both aren't empty
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
        elif l2 :
            tail.next = l2
        
        return temp.next


c = ListNode(3)
b = ListNode(2,c)
a = ListNode(1,b)


z = ListNode(9)
y = ListNode(7,z)
x = ListNode(1,y)



# (head.val)1->2->3->None
print(a.next.val)

head = a.merge(x,a)

# 1->1->2->3->7->9
print(head.next.val)