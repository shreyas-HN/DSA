class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None


class MyCircularDeque:

    def __init__(self, k: int):
        self.left=Node(0)
        self.right=Node(0)
        self.left.next=self.right
        self.right.prev=self.left
        self.space=0
        self.k=k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            need1=self.left.next
            new_node=Node(value)
            self.left.next=new_node
            new_node.prev=self.left
            new_node.next=need1
            need1.prev=new_node
            self.space+=1
            return True



        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            new=Node(value)
            previ=self.right.prev
            previ.next=new
            new.prev=previ
            new.next=self.right
            self.right.prev=new
            self.space+=1
            return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            need=self.left.next
            needed=need.next
            self.left.next=need.next
            need.next.prev=self.left
            self.space-=1
            if self.space==0:
                self.rear=self.left
            self.rear=needed
            
            return True


        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            needlast=self.right.prev
            needlast.prev.next=self.right
            self.right.prev=needlast.prev
            self.space-=1
            return True
        
    

        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.left.next.value

        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.right.prev.value

        

    def isEmpty(self) -> bool:
        return self.left.next==self.right
        

    def isFull(self) -> bool:
        if self.space==self.k:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()