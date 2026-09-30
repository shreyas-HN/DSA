class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        i=0
        d=dict()
        cur=0
        d[cur]=1
        n=len(nums)
        count=0
        while i<n:
            cur+=nums[i]
            r=cur%k
            if r in d:
                
                count+=d[r]
                d[r]+=1
            if r not in d:
                d[r]=1
            i+=1
        return count
        