#Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=head
        if odd:
            even=odd.next
            even_link=even
            while even and even.next:
                next1=even.next.next
                next2=odd.next.next
                odd.next=next2
                even.next=next1
                even=next1
                odd=next2
            odd.next=even_link
            return head
                
            
