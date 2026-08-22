class MyQueue:

    def __init__(self):
        self.queue = []
        self.stack=[]
    def push(self, y):
        self.queue.append(y)

    def pop(self):
        if not self.stack:
            while self.queue:
                self.stack.append(self.queue.pop())
        return self.stack.pop()


    def peek(self):
        if not self.stack:
            while self.queue:
                self.stack.append(self.queue.pop())
        return self.stack[-1]


    def empty(self) -> bool:
        return len(self.stack)==0 and len(self.queue)==0