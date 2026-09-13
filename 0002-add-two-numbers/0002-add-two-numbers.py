# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i=l1
        j=l2
        carry=0
        dummy=ListNode(-1)
        temp=dummy
        while i or j:
            l=0
            r=0
            if i:
                l=i.val
            if j:
                r=j.val
            summ=l+r+carry
            digit=summ%10
            carry=summ//10
            totalsum=ListNode(digit)
            temp.next=totalsum
            temp=totalsum
            if i:
                i=i.next
            if j:
                j=j.next
        if carry:
            x=ListNode(carry)
            temp.next=x
        return dummy.next
        