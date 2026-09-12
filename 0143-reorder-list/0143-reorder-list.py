# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        if s:
            head2=s.next
            head1=head2
            s.next=None
            prev=None
            while head2:
                next_node=head2.next
                head2.next=prev
                prev=head2
                head2=next_node
            i = head
            j = prev
            last = None

            while i and j:
                nexti = i.next
                nextj = j.next

                i.next = j
                j.next = nexti

                last = j

                i = nexti
                j = nextj
        