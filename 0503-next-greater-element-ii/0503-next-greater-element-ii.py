class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        double=n*2
        ans=[-1]*n
        for num in range(double):
            index=num%n
            while stack and nums[index] > nums[stack[-1]]:
                z=stack.pop()
                print(index)
                ans[z]=nums[index]
            stack.append(index)
        return ans