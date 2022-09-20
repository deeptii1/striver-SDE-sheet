# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        while(curr!=None):
            if curr.next and curr.next.val == val:
                curr.next = curr.next.next 
            else:
                curr = curr.next
        
        if head and head.val == val:
            return head.next
        return head
        
        