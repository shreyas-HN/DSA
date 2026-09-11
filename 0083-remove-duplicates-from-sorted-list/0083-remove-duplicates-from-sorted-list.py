# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=head
        if prev:
            i=prev.next
            j=prev.next
            while j:
                if prev.val != j.val:
                    prev.next=j
                    prev=j
                    i=j
                j=j.next
            if prev:
                prev.next=None

        return head
        