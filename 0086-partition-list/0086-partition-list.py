# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        less=ListNode(-1)
        templess=less
        greater=ListNode(-1)
        tempgreat=greater
        i=head
        while i:
            newnode=i.next
            if i.val < x:
                templess.next=i
                templess=templess.next
            else:
                tempgreat.next=i
                tempgreat=tempgreat.next
            i=newnode
        templess.next=greater.next
        tempgreat.next=None
        return less.next





        