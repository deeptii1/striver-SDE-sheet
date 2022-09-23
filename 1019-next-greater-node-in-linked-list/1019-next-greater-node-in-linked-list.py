# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        ptr=head
        while(ptr!=None):
            arr.append(ptr.val)
            ptr=ptr.next
        #print(arr)
        
        stack=[]
        res=[]
        for i in range(len(arr)-1,-1,-1):
            if len(stack)==0:
                res.append(0)
            elif len(stack)>0 and stack[-1]>arr[i]:
                res.append(stack[-1])
            elif (len(stack)>0 and stack[-1]<=arr[i]):
                while(len(stack)>0 and stack[-1]<=arr[i]):
                    stack.pop()
                if len(stack)==0:
                    res.append(0)
                else:
                    res.append(stack[-1])
            stack.append(arr[i])
            
        return res[::-1]
        