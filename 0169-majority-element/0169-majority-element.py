class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        """
        BRUTE FORCE
        n=len(nums)
        fre=n//2
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in d:
            if d[j]>fre:
                return j"""
#MOORES voting algorithms
        n=len(nums)
        candidate=nums[0]
        count=1
        for i in range(1,len(nums)):
            if count==0:
                candidate=nums[i]
            if nums[i]==candidate:
                count+=1
            elif nums[i]!=candidate:
                count-=1
        return candidate
    

            
        