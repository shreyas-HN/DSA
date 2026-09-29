class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ml=0
        n=len(nums)
        i=0
        z=0#1,2,3
        for j in range(n):
            if nums[j]==0:
                z+=1
            while z > k:
                if nums[i]==0:
                    z-=1
                i+=1
            ml=max(ml,j-i+1)
        return ml
                