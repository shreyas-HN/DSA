class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if self.stack2:
            x=self.stack2.pop()
            return x
        else:
            while self.stack1:
                if len(self.stack1)==1:
                    return self.stack1.pop()
                x=self.stack1.pop()
                self.stack2.append(x)
            return None

        

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                x=self.stack1.pop()
                self.stack2.append(x)
        return self.stack2[-1]

        

    def empty(self) -> bool:
        if len(self.stack2)==0 and len(self.stack1)==0:
            return True
        else:
            return False
            
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()