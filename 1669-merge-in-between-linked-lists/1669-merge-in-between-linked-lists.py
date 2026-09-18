# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i=list1
        j=list1
        while a-1:
            i=i.next
            a-=1
        while b+1:
            j=j.next
            b-=1
        last=list2
        while last.next:
            last=last.next
        i.next=list2
        if last:
            last.next=j
        return list1

        