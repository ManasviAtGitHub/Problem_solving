def reorderList(self, head):
        """
        https://leetcode.com/problems/reorder-list/submissions/  

        """
        """
            Input : 1->2->3->4->5->None
            Output : 1->5->2->4->3->None
            
            Idea break into 2 lists,using slow and fast pointer approach
            first: 1->2->3->None     second: 4->5
            
            We reverse the second list ie : second: 5->4->None
            
            Now we merge first and second list 
            by picking one from each list
            
        
        """
        
        #initialize pointers at first and second elements
        #here fast pointer reaches at end or none(if odd no of elements)
        #and second reaches mid way
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #we make the next of slow.next as head of second list
        #also make slow.next to point to None as the last element will be the tail (odd)
        
        
        #second: 4->5->None
        second = slow.next
        
        prev = slow.next = None
        
        #reversing the list (second half)
        while second:
            #tmp = 5, None
            tmp = second.next
            #second.next = None, breaks 4 X> 5, 4->None, 5X>4 5->4->None
            second.next = prev 
            
            #prev = 4, 5
            prev = second
            #second = 5, None
            second = tmp
            
        #merge both lists
        first, second = head, prev #1->2->3->None , 5->4->None
        
        #as second list is guranteed to be smaller than first when odd no of elements are present
        while second:
            #tmp1 = 2, 3 tmp2 = 4, None
            tmp1, tmp2 = first.next, second.next
            
            #1->5, 1->5->2->4
            first.next = second
            #5->2, 4->3... 1->5->2->4->2
            
            second.next = tmp1
            #first = 2, 3 second = 4, None
            first, second = tmp1, tmp2