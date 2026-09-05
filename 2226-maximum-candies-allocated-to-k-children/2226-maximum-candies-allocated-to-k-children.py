class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_give(candies,k,number):
            count=0
            for i in candies:
                if i >= number:
                    count+=(i//number)
                else:
                    continue
            if count >= k:
                return True
            return False

        l=1
        r=sum(candies)//k
        ans=0
        while l<=r:
            mid=(l+r)//2
            if can_give(candies,k,mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
            