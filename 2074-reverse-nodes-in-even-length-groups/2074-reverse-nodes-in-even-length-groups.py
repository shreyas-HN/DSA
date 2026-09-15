# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        group_size=1
        i=head
        p1=i
        p2=p1.next
        while i:
            count=0
            b=None
            while i and count<group_size:
                b=i
                i=i.next
                count+=1
            if count%2==0:
                h=p2
                l=p2
                before=None
                while count and l:
                    nextl=l.next
                    l.next=before
                    before=l
                    l=nextl
                    count-=1
                p1.next=before
                h.next=i
                p1 = h
            else:
                p1 = b
            group_size+=1
            p2=i
        return head
            
            


        