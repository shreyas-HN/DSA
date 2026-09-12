# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        if head is None:
            return head
        fast=head
        while k%length:
            fast=fast.next
            k-=1
        slow=head
        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        fast.next=head
        head=slow.next
        slow.next=None
        return head
        
        
        