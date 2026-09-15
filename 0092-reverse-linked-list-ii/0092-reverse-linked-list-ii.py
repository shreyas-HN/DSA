# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i=head
        j=head
        diff=right-left+1
        prev=None
        while left-1 and i:
            prev=i
            i=i.next
            left-=1
        while right-1 and j:
            j=j.next
            right-=1
        h=i
        l=i
        r=j
        p=prev
        before=None
        if r:
            next1=r.next
        else:
            next1=None
        while diff:
            nextl=l.next
            l.next=before
            before=l
            l=nextl
            diff-=1
        if p:
            p.next = before
        else:
            head = before
        h.next=next1
        return head





        


        