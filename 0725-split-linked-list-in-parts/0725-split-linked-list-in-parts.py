# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        i=head
        n=0
        while i:
            n+=1
            i=i.next
        base=n//k
        extra=n%k
        j=head
        ans=[]
        leng=0
        for p in range(k):
            ans.append(j)
            if extra!=0:
                leng=base+1
                extra-=1
            else:
                leng=base
            for n in range(leng-1):
                j=j.next
                leng-=1
            if j:
                next_part = j.next
                j.next = None
                j = next_part
        return ans






        