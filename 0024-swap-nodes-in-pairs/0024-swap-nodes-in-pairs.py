# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        prev = None

        if i and i.next:
            head = i.next

        while i and i.next:
            j = i.next
            nexti = j.next

            j.next = i
            i.next = nexti

            if prev:
                prev.next = j

            prev = i
            i = nexti

        return head
                    
        