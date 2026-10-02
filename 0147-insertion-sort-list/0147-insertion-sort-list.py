# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        dummy=ListNode(-111)
        dummy.next=head
        if head:
            i=head.next
        else:
            return head
        previ=head
        while i:
            nexti=i.next
            if previ.val < i.val:
                previ=i
                i=i.next
                continue
            j=dummy.next
            prev=dummy
            while j:
                nextj=j.next
                moved = False
                if j.val>i.val:
                    previ.next=nexti
                    prev.next=i
                    i.next=j
                    prev=j
                    j=nextj
                    moved = True
                    break
                prev=j
                j=nextj
            if not moved:
                previ=i
            i=nexti
        return dummy.next

                


        
        