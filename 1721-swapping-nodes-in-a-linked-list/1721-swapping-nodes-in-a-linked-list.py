# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i=head
        numi=k-1
        while numi and i:
            i=i.next
            numi-=1
        numf=k
        fast=head
        while numf and fast:
            fast=fast.next
            numf-=1
        slow=head
        while fast:
            fast=fast.next
            slow=slow.next
        temp1=slow.val
        temp2=i.val
        i.val=temp1
        slow.val=temp2
        return head
        

        