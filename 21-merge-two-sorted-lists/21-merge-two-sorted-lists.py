# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode=ListNode(0)
        dd=dummynode
        while(True):
            
            if list1 is None:
                dd.next=list2
                break

            if list2 is None:
                dd.next=list1
                break

        
            if list1.val<=list2.val:
                dd.next=list1
                list1=list1.next
            else:
                dd.next=list2
                list2=list2.next
            dd=dd.next
        
        return(dummynode.next)
            
        
        