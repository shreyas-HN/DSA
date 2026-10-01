class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        i=0
        d=dict()
        cur=0
        d[0]=1
        count=0
        while i<len(nums):
            cur += nums[i]
            diff=cur - goal
            if diff in d:
                count += d[diff]

            if cur not in d:
                d[cur] = 1
            else:
                d[cur] += 1
            i+=1
        return count
