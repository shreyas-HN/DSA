class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i,j in enumerate(temperatures):
            while len(stack) != 0 and j > temperatures[stack[-1]]:
                index=stack.pop()
                adding=i-index
                ans[index]=adding
            stack.append(i)
        return ans
                