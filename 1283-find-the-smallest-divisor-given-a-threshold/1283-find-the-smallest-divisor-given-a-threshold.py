import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def getsumbydivisor(nums,divisor):
            summ=0
            for i in nums:
                summ+=math.ceil(i/divisor)
            return summ
        l = 1
        r = max(nums)
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            x = getsumbydivisor(nums, mid)

            if x > threshold:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1

        return ans

        