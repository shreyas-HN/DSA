class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            ind=abs(nums[i])-1
            if nums[ind]>0:
                nums[ind]=-1*nums[ind]
        for j in range(n):
            if nums[j] > 0:
                ans.append(j+1)
        return ans
        