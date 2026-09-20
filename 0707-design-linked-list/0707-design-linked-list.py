class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class MyLinkedList:
    #I wanna do it doubly linked list, yeap letsgoooooooooooooooooooooooooo!
    def __init__(self):
        self.left=Node(0)
        self.right=Node(0)
        self.left.next=self.right
        self.right.prev=self.left
        
    def get(self, index: int) -> int:
        curr=self.left.next
        while curr and index>0:
            curr=curr.next
            index-=1
        if curr!=None and curr is not self.right and index==0:
            return curr.val
        else:
            return -1
        
        

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        prev1=self.left
        next1=prev1.next
        prev1.next=new_node
        new_node.next=next1
        new_node.prev=prev1
        next1.prev=new_node


        

    def addAtTail(self, val: int) -> None:
        new_Node=Node(val)
        tail=self.right
        prev1=tail.prev
        prev1.next=new_Node
        new_Node.next=tail
        tail.prev=new_Node
        new_Node.prev=prev1
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_nnode=Node(val)
        head=self.left.next
        while head and index>0:
            head=head.next
            index-=1
        if index==0:
            previ=head.prev
            previ.next=new_nnode
            new_nnode.next=head
            head.prev=new_nnode
            new_nnode.prev=previ
        


        

    def deleteAtIndex(self, index: int) -> None:
        head=self.left.next
        while head and index>0:
            head=head.next
            index-=1
        if head is not self.right:
            previous=head.prev
            nextone=head.next
            previous.next=nextone
            nextone.prev=previous
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)