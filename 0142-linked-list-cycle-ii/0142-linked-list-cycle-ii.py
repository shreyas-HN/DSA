# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=head
        f=head
        while f and f.next:
            f=f.next.next
            s=s.next
            if f==s:
                p=head
                q=f
                while p!=q:
                    p=p.next
                    q=q.next
                return p