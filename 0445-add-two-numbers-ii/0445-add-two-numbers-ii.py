# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        list2=[]
        curr=l1
        while curr:
            list1.append(curr.val)
            curr=curr.next
        curr2=l2
        while curr2:
            list2.append(curr2.val)
            curr2=curr2.next
        carry=0
        temp=None
        while list1 or list2 or carry:
            d1=0
            d2=0
            if list1:
                d1=list1.pop()
            if list2:
                d2=list2.pop()
            summ=d1+d2+carry
            digit=summ%10
            carry=summ//10
            new_node=ListNode(digit)
            new_node.next=temp
            temp=new_node
        return temp


            





        