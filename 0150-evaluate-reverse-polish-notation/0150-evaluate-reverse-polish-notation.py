class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "+-/*":
                stack.append(i)
            else:
                x = int(stack.pop())
                y = int(stack.pop())
                if i=="+":
                    z=x+y
                    stack.append(z)
                elif i=="-":
                    z=y-x
                    stack.append(z)
                elif i=="*":
                    z=x*y
                    stack.append(z)
                else:
                    z=int(y/x)
                    stack.append(z)
        return int(stack.pop())
                