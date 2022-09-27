# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        def reverse(head):
            prev= None
            next = None
            curr = head 
            while(curr!=None):
                next = curr.next 
                curr.next = prev 
                prev = curr
                curr = next 
                
            
            return prev 
        
        
        
        
        curr = head 
        prev = None
        count = 1  
        while(count!=left):
            prev = curr
            curr = curr.next 
            count+=1 
            
        start = curr 
        while(count!=right):
            curr = curr.next 
            count+=1 
            
        rest = curr.next 
        curr.next = None
        
        newhead = reverse(start)
        
        if prev!=None:
            prev.next = newhead
            
        curr = newhead 
        while(curr.next!=None):
            curr = curr.next 
            
        curr.next = rest
        
        if left == 1:
            return newhead
        else:
            return head
        
            
        
        