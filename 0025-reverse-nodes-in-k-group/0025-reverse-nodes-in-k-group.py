# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        total=0
        p=head
        while p:
            total+=1
            p=p.next
        i=head
        j=head
        p=None
        c=total//k
        while c:
            r=i
            count=0
            while j and count < k:
                j=j.next
                count+=1
            l=i
            before=None
            count1=0
            while count1<k:
                nextl=l.next
                l.next=before
                before=l
                l=nextl
                count1+=1
            if p:
                p.next=before
            else:
                head=before
            r.next=j
            p=r
            i=j
            c-=1
        p.next=j
        return head
            
            



            



        