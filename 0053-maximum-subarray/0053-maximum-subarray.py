class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi=-23223232323
        curr_sum=0
        for i in nums:
            curr_sum+=i
            if curr_sum>maxi:
                maxi=curr_sum
            if curr_sum<0:
                curr_sum=0
        return maxi
        