class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        total_sum=(n*(n+1))/2
        ans=int(total_sum-sum(nums))
        return ans
        