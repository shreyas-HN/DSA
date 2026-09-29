class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #THIS code takes 0(n) space complextity but we need in O(1)
        """n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            suffix[j]=suffix[j+1]*nums[j+1]
        for k in range(n):
            s=prefix[k]*suffix[k]
            prefix[k]=s
        return prefix"""
        n=len(nums)
        prefix=[1]*n
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        suffix_p=1
        for j in range(n-1,-1,-1):
            prefix[j]*=suffix_p
            suffix_p*=nums[j]
        return prefix
        

        