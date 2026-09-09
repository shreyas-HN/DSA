# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1=0
        c1=headA
        while c1:
            c1=c1.next
            l1+=1
        l2=0
        c2=headB
        while c2:
            c2=c2.next
            l2+=1
        i=headA
        j=headB
        diff=abs(l1-l2)
        if l1>l2:
            while diff:
                i=i.next
                diff-=1
        if l2 > l1:
            while diff:
                j=j.next
                diff-=1
        while i and j:
            if i==j:
                return i
            i=i.next
            j=j.next

        

        