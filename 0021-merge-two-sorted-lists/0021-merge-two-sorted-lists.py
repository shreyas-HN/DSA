# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i=list1
        j=list2
        dummy=ListNode(-1)
        temp=dummy
        while i and j:
            if j.val < i.val:
                nextj=j.next
                temp.next=j
                temp=j
                j=nextj
            else:
                nexti=i.next
                temp.next=i
                temp=i
                i=nexti
        if i:
            temp.next=i
        if j:
            temp.next=j
        return dummy.next




            

        
            



        