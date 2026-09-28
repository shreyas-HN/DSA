class Solution:
    def majorityElement(self, nums: list[int]) -> int:
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
                return j
            
        