# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        l=0
        i=head
        arr=[]
        while i:
            l+=1
            arr.append(i.val)
            i=i.next
        stack=[]
        ans=[0]*l
        for i in range(len(arr)):
            while stack and arr[stack[-1]]<arr[i]:
                z=stack.pop()
                ans[z]=arr[i]
            stack.append(i)
        return ans
            
        

        