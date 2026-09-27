class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i=0
        d=dict()
        cur=0
        d[cur]=1
        n=len(nums)
        count=0
        while i<n:
            cur+=nums[i]
            diff=cur-k
            if diff in d:
                count+=d[diff]
            if cur not in d:
                d[cur]=1
            else:
                d[cur]+=1
            i+=1
        return count


        