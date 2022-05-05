class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(self, head):
        prev = None
        while head != None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


c = ListNode(3)
b = ListNode(2,c)
a = ListNode(1,b)

# (head.val)1->2->3->None
print(a.val)

head = a.reverseList(a)

# None<-1<-2<-3(head.val)
print(head.val)