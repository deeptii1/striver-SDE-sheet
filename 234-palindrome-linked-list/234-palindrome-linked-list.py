# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        arr=[]
        ptr=head
        while(ptr!=None):
            arr.append(ptr.val)
            ptr=ptr.next
        #print(arr)
        
        def check(arr):
            start=0
            end=len(arr)-1
            while(start<end):
                if arr[start]!=arr[end]:
                    return False
                start+=1
                end-=1
            return True
        
        return check(arr)
        '''
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
        
        prev=None
        curr=slow
        while curr!=None:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
         
        #print(curr)
        #print(prev)
        
        while(prev!=None):
            if prev.val!=head.val:
                return False
            prev=prev.next
            head=head.next
        return True
            
        
            