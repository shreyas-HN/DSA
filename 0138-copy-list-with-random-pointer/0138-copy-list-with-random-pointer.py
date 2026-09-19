"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        i=head
        curr=head
        while curr:
            nnode=curr.next
            new_node=Node(curr.val)
            new_node.next=nnode
            curr.next=new_node
            curr=nnode
        c1 = head
        if c1:
            c2 = head.next

            while c1 and c2:
                if c1.random:
                    c2.random = c1.random.next

                c1 = c2.next

                if c1:
                    c2 = c1.next
        oldhead=head
        if oldhead:
            newhead=head.next
            p1=oldhead
            p2=newhead
            while p1 and p2:
                next_node=p2.next
                p1.next=next_node
                if next_node:
                    p2.next = next_node.next
                else:
                    p2.next = None
                p1=next_node
                if next_node:
                    p2=next_node.next
            return newhead



