# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        k = head
        j = head

        # Find middle
        while j and j.next:
            k = k.next
            j = j.next.next

        # Odd length → skip middle
        if j is not None:
            k = k.next

        # Reverse second half
        prev = None
        while k:
            next_n = k.next
            k.next = prev
            prev = k
            k = next_n

        # Compare first half with reversed second half
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
            
            