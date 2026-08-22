class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for num in asteroids:
            while stack and (stack[-1]>0 and num<0):
                last=stack.pop()
                if last>abs(num):
                    stack.append(last)
                    break
                elif last==abs(num):
                    break
            else:
                stack.append(num)

        return stack
                