class Solution:
    def isValid(self, s: str) -> bool:
        d={"(":")","[":"]","{":"}"}
        stack=[]
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if len(stack)==0 or c!=d[stack.pop()]:
                    return False
        return len(stack)==0
                