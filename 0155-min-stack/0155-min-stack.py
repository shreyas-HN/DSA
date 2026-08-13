class MinStack:

    def __init__(self):
        self.stack = []
        self.Getmin=[]

    def push(self, value):
        self.stack.append(value)
        if len(self.Getmin)==0:
            self.Getmin.append(value)
        else:
            val=min(value,self.Getmin[-1])
            self.Getmin.append(val)



    def pop(self):
        if self.stack:
            self.stack.pop()
            self.Getmin.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.Getmin[-1]
