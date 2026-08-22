from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
    def push(self, x):
        self.q1.append(x)

    def pop(self):
        for _ in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())
        return self.q1.popleft()

    def top(self):
        for _ in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())
        y=self.q1[0]
        x = self.q1.popleft()
        self.q1.append(x)
        return y

    def empty(self):
        return len(self.q1)==0