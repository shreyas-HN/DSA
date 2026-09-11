# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        i=head
        j=head
        while j and j.next:
            i=i.next
            j=j.next.next
        if j is not None:
            i=i.next
        prev=None
        while i:
            next_node=i.next
            i.next=prev
            prev=i
            i=next_node
        left=head
        right=prev
        while left and right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True